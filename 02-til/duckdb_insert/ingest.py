import sqlite3
import pandas as pd
import duckdb
import click
import mysql.connector
import psycopg2
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, SSLError


def connect_to_s3(aws_profile):
    """
    Connects to AWS S3 using the specified profile.
    """
    print(f'Connecting to AWS S3 using profile {aws_profile}')
    boto3.setup_default_session(profile_name=aws_profile)
    try:
        return boto3.client('s3')
    except (NoCredentialsError, PartialCredentialsError, SSLError) as e:
        print(f'An error occurred while connecting to S3: {e}')
        return None


def write_to_s3(file_name, bucket, object_name=None, s3_client=None):
    """
    Uploads a file to AWS S3 using a multipart upload.
    """
    if object_name is None:
        object_name = file_name
    try:
        config = boto3.s3.transfer.TransferConfig(
            multipart_threshold=10242*5)  # 5MB
        _ = s3_client.upload_file(
            file_name, bucket, object_name, Config=config)  # 5MB
        print(f'Successfully uploaded {file_name} to {bucket}/{object_name}')
        return True
    except Exception as e:
        print(f'An error occurred: {e}')
        return False


def get_prefix_and_path(target_path):
    """ Returns the prefix and path for an S3 path. """
    bucket = target_path[5:].split('/')[0]
    s3_prefix = target_path[6:][len(bucket):]
    return bucket, s3_prefix


def del_s3_files(bucket, prefix, s3_client):
    """ Deletes all files with the given prefix in the given bucket. """
    # test if prefix exists has at least 3 levels
    nb_level = prefix.count('/')
    if nb_level < 2:
        print(f"prefix {prefix} is too short, not deleting")
        return
    response = s3_client.list_objects_v2(Bucket=bucket, Prefix=prefix)

    if 'Contents' in response:
        for obj in response['Contents']:
            print(f"Deleting {obj['Key']}")
            s3_client.delete_object(Bucket=bucket, Key=obj['Key'])


def write_to_parquet(data_generator, parquet_file_prefix, target_path, s3_client=None):
    """ Write data from a generator to Parquet files. """
    bucket, s3_prefix = get_prefix_and_path(target_path)
    conn = duckdb.connect(database=':memory:', read_only=False)
    for i, data in enumerate(data_generator):
        # generate an uuid for the file
        file_name = f'{parquet_file_prefix}_{i}.parquet'
        print(f'Writing {file_name}')
        conn.register('batch', data)
        conn.execute('CREATE TABLE data AS SELECT * FROM batch')
        if target_path.startswith('s3:'):
            target_file = f'/tmp/{file_name}'
            conn.execute(f"COPY data TO '{target_file}' (FORMAT PARQUET)")
            s3_path = f'{s3_prefix}/{file_name}'
            # print(f"prefix: {s3_prefix}, path: {s3_path}")
            print(f'Uploading {target_file} to s3://{bucket}/{s3_path}')
            write_to_s3(target_file, bucket, s3_path, s3_client=s3_client)
            os.remove(target_file)
        else:
            conn.execute(
                f"COPY data TO '{target_path}/{file_name}' (FORMAT PARQUET)")
        conn.execute('DROP TABLE data')
        conn.unregister('batch')
    conn.close()


def connect_to_sqlite(database):
    """
    Connects to a SQLite database.

    Args:
        database (str): The path to the SQLite database.

    Returns:
        sqlite3.Connection: A connection object to the SQLite database.
    """
    print(f'Connecting to SQLite database {database}')
    return sqlite3.connect(database)


def connect_to_db(db_type, host=None,port=None, user=None, password=None, database=None):
    """
    Connects to a database based on the db_type.
    """
    if db_type == 'mysql':
        print(f'Connecting to MySQL database {database}')
        return mysql.connector.connect(host=host, user=user, password=password, database=database, port=port)
    elif db_type == 'postgres':
        print(f'Connecting to PostgreSQL database {database}')
        return psycopg2.connect(host=host, database=database, user=user, password=password, port=port)
    elif db_type == 'sqlite':
        print(f'Connecting to SQLite database {database}')
        return sqlite3.connect(database)
    else:
        raise ValueError(f'Unsupported database type: {db_type}')


def read_data_in_batches(connection, query, batch_size):
    """
    Reads data from a database connection in batches.

    Args:
        connection: A database connection object.
        query: A SQL query string to execute.
        batch_size: The number of rows to fetch per batch.

    Yields:
        A pandas DataFrame containing the fetched rows.
    """
    cursor = connection.cursor()
    cursor.execute(query)
    while True:
        rows = cursor.fetchmany(batch_size)
        if not rows:
            break
        data = pd.DataFrame(rows, columns=[column[0]
                            for column in cursor.description])
        yield data


@click.command()
@click.option('--host', required=False, help='The host of the database server.')
@click.option('--port', required=False, help='The port of the database server.')
@click.option('--user', required=False, help='The username to connect to the database server.')
@click.option('--password', required=False, help='The password to connect to the database server.')
@click.option('--db_type', default='sqlite', help='The type of the database possible value: sqlite,mysql, or postgres.')
@click.option('--database', required=lambda: not install_only, help='The name of the database.')
@click.option('--table_name', required=lambda: not install_only, help='The name of the table.')
@click.option('--batch_size', default=100000, help='The batch size.')
@click.option('--target_path', default='./data', help='The target path for the Parquet files.')
@click.option('--aws_profile', default=None, help='The AWS profile to use for S3.')
@click.option('--start_date', default=None, help='The start date to filter the SQL query.')
@click.option('--end_date', default=None, help='The end date to filter the SQL query.')
@click.option('--delete_files', default=False, help='Delete the target files if set to true.')
@click.option('--createdat_column', default=None, help='The name of the column containing the creation date of the record')
def main(host,port, user, password, db_type, database, table_name, batch_size, target_path, aws_profile, start_date, end_date, delete_files, createdat_column):
    """ Ingest data from a database table and write it to a parquet file. """

    # Connect to the database
    connection = connect_to_db(db_type, host,port, user, password, database)

    # Construct the SQL query
    query = f"SELECT * FROM {table_name}"
    if start_date and end_date and createdat_column:
        # replace 'date_column' with the actual date column in your table
        query += f" WHERE {createdat_column} BETWEEN '{start_date}' AND '{end_date}'"

    # Read data in batches
    data_generator = read_data_in_batches(connection, query, batch_size)

    # Create the target directory if it doesn't exist
    if not os.path.exists(target_path) and not target_path.startswith('s3:'):
        os.mkdir(target_path)

    # Connect to S3 if the target path is an S3 URI
    s3_client = None
    if target_path.startswith('s3:'):
        if aws_profile:
            s3_client = connect_to_s3(aws_profile)
        else:
            s3_client = boto3.client('s3')
        if s3_client is None:
            print('Failed to connect to S3. Exiting...')
            return

    # Delete the target files if delete_files is set to true
    if delete_files:
        bucket, prefix = get_prefix_and_path(target_path)
        if bucket and prefix:
            del_s3_files(bucket, prefix, s3_client)

    # Write data to Parquet files
    ingestion_date = pd.Timestamp.now().strftime('%Y%m%d%H%M%S')
    parquet_file_prefix = f'{ingestion_date}_{table_name}'
    write_to_parquet(data_generator=data_generator, parquet_file_prefix=parquet_file_prefix,
                     target_path=target_path, s3_client=s3_client)


if __name__ == '__main__':
    main()
