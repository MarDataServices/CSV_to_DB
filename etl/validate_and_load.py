import os
import psycopg2
from psycopg2 import sql

from extract import extract_data

#Connection to database
conn = psycopg2.connect(
    db_name = "example_db",
    host = "example_host",
    port = "5432",
    user = "admin",
    password = "admin"
)
cursor = conn.cursor()

def transform_data(data_dir):
    for file in os.listdir(data_dir):
        if file.endswith('.csv'):
            extract_data(file)
            with open(file, 'r') as f:
                cursor.copy_expert(sql.SQL("COPY {} from STDIN WITH CSV HEADER").format(sql.Identifier(file.split('.')[0])), f)
            conn.commit()

cursor.close()
conn.close()

