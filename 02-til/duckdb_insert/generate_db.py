import sqlite3
import sys
from faker import Faker
import random
from datetime import datetime, timedelta

def create_connection(database):
    conn = sqlite3.connect(database)
    return conn

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                        id INTEGER PRIMARY KEY,
                        business_id INTEGER,
                        description TEXT,
                        price REAL,
                        created_at TIMESTAMP,
                        updated_at TIMESTAMP)''')
    conn.commit()

def insert_fake_data(conn, num_rows):
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
                          VALUES (?, ?, ?, ?, ?)''', (business_id, description, price, created_at, updated_at))

    conn.commit()

def main(database, num_rows):
    conn = create_connection(database)
    create_table(conn)
    insert_fake_data(conn, num_rows)
    conn.close()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python generate_fake_data.py <database_name> <number_of_rows>")
        sys.exit(1)

    database = sys.argv[1]
    num_rows = int(sys.argv[2])
    main(database, num_rows)
