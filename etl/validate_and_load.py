import os
import sys
import psycopg2
import csv
from psycopg2 import sql

import extract as et

def transform_data(data_dir, con, cur):
    for file in os.listdir(data_dir):
        if file.endswith('.csv'):
            path = os.path.join(data_dir, file)
            et.extract_data(path)
            
            table_name = file.split('.')[0]
            

            
            with open(path, 'r') as f:
                reader = csv.reader(f)
                headers = next(reader)
                
            with open(path, 'r') as f:    
                columns = [sql.SQL("{} TEXT").format(sql.Identifier(col.strip())) for col in headers]
                drop_all = sql.SQL("DROP TABLE {}".format(table_name))
                create_tbl = sql.SQL("CREATE TABLE {} ({});").format(
                    sql.Identifier(table_name),
                    sql.SQL(", ").join(columns)
                )
                cur.execute(drop_all)
                cur.execute(create_tbl)
                
                
                
                cur.copy_expert(sql.SQL("COPY {} from STDIN WITH CSV HEADER").format(sql.Identifier(file.split('.')[0])), f)

    con.commit()

def main():
    #Connection to database
    conn = psycopg2.connect(
        dbname = "example",
        host = "localhost",
        port = "5432",
        user = "example",
        password = "example"
    )
    cursor = conn.cursor()
    
    try:
        transform_data(sys.argv[1], conn, cursor)
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    main()