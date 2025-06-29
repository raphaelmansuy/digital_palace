import sys
import click
import sqlite3
from faker import Faker
import random
from datetime import datetime, timedelta
import psycopg2
import mysql.connector


def create_connection(database, user, password, host, db_type):
    """
    Create a connection to the specified database.

    Args:
        database (str): The name of the database.
        user (str): The username used to authenticate.
        password (str): The password used to authenticate.
        host (str): The host of the database.
        db_type (str): The type of the database. Can be 'postgres', 'mysql', or 'sqlite'.

    Returns:
        Connection: A connection to the database.
    """
    conn = None
    if db_type == 'postgres':
        conn = psycopg2.connect(
            database=database, user=user, password=password, host=host)
    elif db_type == 'mysql':
        conn = mysql.connector.connect(
            user=user, password=password, host=host, database=database)
    elif db_type == 'sqlite':
        conn = sqlite3.connect(database)
    else:
        print("Invalid database type. Please choose from 'postgres', 'mysql', or 'sqlite'.")
        sys.exit(1)
    return conn


def create_table(conn):
    """
    Creates a new table named 'products' in the given database connection if it does not exist already.

    Args:
        conn: A database connection object.

    Returns:
        None
    """
    cursor = conn.cursor()
    # Drop table if it exists
    cursor.execute('DROP TABLE IF EXISTS products')
    cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                        id SERIAL PRIMARY KEY,
                        business_id INTEGER,
                        description TEXT,
                        price REAL,
                        created_at TIMESTAMP,
                        updated_at TIMESTAMP)''')
    conn.commit()


def insert_fake_data(conn, num_rows):
    """ Inserts fake data into the 'products' table of the given database connection. Args: conn (duckdb.Connection): The database connection to use. num_rows (int): The number of rows to insert. Returns: None """
    fake = Faker()
    cursor = conn.cursor()
    for index in range(num_rows):
        business_id = random.randint(1, 100000000)
        description = fake.sentence()
        price = round(random.uniform(10, 1000), 2)
        created_at = fake.date_between(start_date='-1y', end_date='today')
        updated_at = created_at + timedelta(days=random.randint(0, 365))
        if index % 100000 == 0:
            print(f'Inserted {index} rows')
        cursor.execute('''INSERT INTO products (business_id, description, price, created_at, updated_at) 
                          VALUES (%s, %s, %s, %s, %s)''',
                       (business_id, description, price, created_at, updated_at))
    conn.commit()


@click.command()
@click.option('--database', prompt='Database name', help='The name of the database.')
@click.option('--user', prompt='User', help='The username used to authenticate.')
@click.option('--password', prompt='Password', help='The password used to authenticate.')
@click.option('--host', prompt='Host', help='The host of the database.')
@click.option('--db_type', prompt='Database type', help="The type of the database. Can be 'postgres', 'mysql', or 'sqlite'.")
@click.option('--num_rows', prompt='Number of rows', help='The number of rows of fake data to insert into the table.', default=1000000)
def run(database, user, password, host, db_type, num_rows):
    """
    Creates a connection to the specified database, creates a table, inserts fake data, and closes the connection.

    Args:
        database (str): The name of the database.
        user (str): The username used to authenticate.
        password (str): The password used to authenticate.
        host (str): The host of the database.
        db_type (str): The type of the database. Can be 'postgres', 'mysql', or 'sqlite'.
        num_rows (int): The number of rows of fake data to insert into the table.
    """
    conn = create_connection(database, user, password, host, db_type)
    create_table(conn)
    insert_fake_data(conn, num_rows)
    conn.close()


if __name__ == '__main__':
    run()
