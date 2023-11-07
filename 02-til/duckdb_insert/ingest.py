import os
import sqlite3
import pandas as pd
import duckdb
import click
import mysql.connector
import psycopg2

import boto3
from botocore.exceptions import NoCredentialsError

def connect_to_s3(aws_profile):
    """ Connects to AWS S3 using the specified profile. """
    boto3.setup_default_session(profile_name=aws_profile)
    return boto3.client('s3')

def write_to_s3(file_name, bucket, object_name=None):
    """ Uploads a file to AWS S3 using a multipart upload. """
    if object_name is None:
        object_name = file_name

    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name, Config=boto3.s3.transfer.TransferConfig(multipart_threshold=1024**2*5)) # 5MB
    except NoCredentialsError:
        print("No AWS credentials found.")
        return False
    return True

def write_to_parquet(data_generator, parquet_file_prefix, target_path, s3_client=None, bucket=None):
    """ Write data from a generator to Parquet files. """
    conn = duckdb.connect(database=':memory:', read_only=False)
    for i, data in enumerate(data_generator):
        file_name = f'{parquet_file_prefix}_{i}.parquet'
        print(f'Writing {file_name}')
        conn.register('batch', data)
        conn.execute('CREATE TABLE data AS SELECT * FROM batch')
        if target_path.startswith('s3:'):
            target_file = f'/tmp/{file_name}'
            conn.execute(f"COPY data TO '{target_file}' (FORMAT PARQUET)")
            write_to_s3(target_file, bucket, f'{target_path[4:]}/{file_name}')
            os.remove(target_file)
        else:
            conn.execute(f"COPY data TO '{target_path}/{file_name}' (FORMAT PARQUET)")
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


def connect_to_mysql(host, user, password, database):
    """ 
    Connects to a MySQL database with the given database name.
    Args:
        host (str): The host of the MySQL server.
        user (str): The username to connect to the MySQL server.
        password (str): The password to connect to the MySQL server.
        database (str): The name of the database to connect to.
    Returns:
        mysql.connector.connection_cext.CMySQLConnection: A connection object representing the connection to the database.
    """
    print(f'Connecting to MySQL database {database}')
    return mysql.connector.connect(host=host, user=user, password=password, database=database)

def connect_to_postgres(host, user, password, database):
    """ 
    Connects to a PostgreSQL database.
    Args:
        host (str): The host of the PostgreSQL server.
        user (str): The username to connect to the PostgreSQL server.
        password (str): The password to connect to the PostgreSQL server.
        database (str): The name of the database to connect to.
    Returns:
        psycopg2.extensions.connection: A connection object representing the connection to the database.
    """
    print(f'Connecting to PostgreSQL database {database}')
    return psycopg2.connect(host=host, database=database, user=user, password=password)

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


def write_to_parquet(data_generator, parquet_file_prefix, target_path, s3_client=None, bucket=None):
    """ Write data from a generator to Parquet files. """
    conn = duckdb.connect(database=':memory:', read_only=False)
    for i, data in enumerate(data_generator):
        file_name = f'{parquet_file_prefix}_{i}.parquet'
        print(f'Writing {file_name}')
        conn.register('batch', data)
        conn.execute('CREATE TABLE data AS SELECT * FROM batch')
        if target_path.startswith('s3:'):
            target_file = f'/tmp/{file_name}'
            conn.execute(f"COPY data TO '{target_file}' (FORMAT PARQUET)")
            write_to_s3(target_file, bucket, f'{target_path[4:]}/{file_name}')
            os.remove(target_file)
        else:
            conn.execute(f"COPY data TO '{target_path}/{file_name}' (FORMAT PARQUET)")
        conn.execute('DROP TABLE data')
        conn.unregister('batch')
    conn.close()

@click.command()
@click.option('--host', required=True, help='The host of the database server.')
@click.option('--user', required=True, help='The username to connect to the database server.')
@click.option('--password', required=True, help='The password to connect to the database server.')
@click.option('--db_type', default='sqlite', help='The type of the database possible value: sqlite,mysql, or postgres.')
@click.option('--database', required=True, help='The name of the database.')
@click.option('--table_name', required=True, help='The name of the table.')
@click.option('--batch_size', default=100000, help='The batch size.')
@click.option('--target_path', default='./data', help='The target path for the Parquet files.')
@click.option('--aws_profile', default=None, help='The AWS profile to use for S3.')
@click.option('--bucket', default=None, help='The S3 bucket to use.')
def main(host, user, password, db_type, database, table_name, batch_size, target_path, aws_profile, bucket):
    if db_type == 'mysql':
        connection = connect_to_mysql(host, user, password, database)
    elif db_type == 'postgres':
        connection = connect_to_postgres(host, user, password, database)
    elif db_type == 'sqlite':
        connection = connect_to_sqlite(database)
    else:
        raise ValueError(f'Unsupported database type: {db_type}')

    data_generator = read_data_in_batches(connection, f"SELECT * FROM {table_name}", batch_size)

    if not os.path.exists(target_path) and not target_path.startswith('s3:'):
        os.mkdir(target_path)

    s3_client = None
    if target_path.startswith('s3:') and aws_profile and bucket:
        s3_client = connect_to_s3(aws_profile)

    write_to_parquet(data_generator=data_generator, parquet_file_prefix=table_name, target_path=target_path, s3_client=s3_client, bucket=bucket)

if __name__ == '__main__':
    main()