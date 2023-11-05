import os 
import pandas as pd
import duckdb
import sqlite3


def connect_to_sqlite(database):
    """
    Connect to a SQLite database.

    Parameters:
    database (str): The database name.

    Returns:
    sqlite3.Connection: The database connection.
    """
    print(f'Connecting to {database}')
    return sqlite3.connect(database)


def read_data_in_batches(connection, query, batch_size):
    """
    Read data from a database in batches.

    Parameters:
    connection (sqlite3.Connection): The database connection.
    query (str): The SQL query.
    batch_size (int): The batch size.

    Returns:
    Generator[pd.DataFrame, None, None]: A generator that yields dataframes.
    """
    cursor = connection.cursor()
    cursor.execute(query)
    while True:
        rows = cursor.fetchmany(batch_size)
        if not rows:
            break
        data = pd.DataFrame(rows, columns=[column[0] for column in cursor.description])
        yield data



def write_to_parquet(data_generator, parquet_file_prefix,target_path):
    """
    Write data to a Parquet file using DuckDB.

    Parameters:
    data_generator (Generator[pd.DataFrame, None, None]): The data generator.
    parquet_file_prefix (str): The Parquet file path prefix.
    """
    conn = duckdb.connect(database=':memory:', read_only=False)
    for i, data in enumerate(data_generator):
        file_name = f'{parquet_file_prefix}_{i}.parquet'
        print(f'Writing {file_name}')
        conn.register('batch', data)
        conn.execute(f'CREATE TABLE data AS SELECT * FROM batch')
        conn.execute(f"COPY data TO '{target_path}/{file_name}' (FORMAT PARQUET)")
        conn.execute('DROP TABLE data')
        conn.unregister('batch')
    conn.close()


def main():
    table_name = 'products'
    batch_size = 1000000
    target_path = './data'
    parquet_file_prefix = 'my_data'
    connection = connect_to_sqlite('testdb.sqlite')
    data_generator = read_data_in_batches(connection, f"SELECT * FROM {table_name}", batch_size)
    # create directory to store parquet files if it doesn't exist
    if not os.path.exists(target_path):
      os.mkdir(target_path)
    write_to_parquet(data_generator=data_generator, parquet_file_prefix=parquet_file_prefix,target_path=target_path)


if __name__ == '__main__':
    main()
