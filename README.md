# CSV to Database pipeline
This tool facilitates the transfer of data from a CSV file into a database. This tool does not depend on a specific set of CSV files, but instead adds tables dynamically consisting of the existing columns and using the name of the file in question. 

## Usage
If you already have a database set up, you can change the 'conn' variable in 'validate_and_load.py' to match your database and the credentials of an admin user.

If not, you could set up a new postgresql database locally on your machine:
``` sh
    createdb example
    psql postgres

    CREATE DATABASE example;
    CREATE USER example WITH PASSWORD 'example';
    GRANT ALL PRIVILEGES ON DATABASE example TO example;
    \q
```

Now you should be able to run the CSV to Database pipeline by typing in the following in your CLI:
``` sh
    #Installing necessary dependencies
    python3 -m pip install psycopg2 pandas
    #Running the script
    python3 ./etl/validate_and_load.py ./data/
```
