import os
import pandas as pd
import mysql.connector
from mysql.connector import Error
from sqlalchemy import create_engine
import argparse

def connect_mysql(host, user, password, database=None):
    """Connect to MySQL and create database if it doesn't exist"""
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        
        cursor = connection.cursor()
        
        # Create database if it doesn't exist
        if database:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
            cursor.execute(f"USE {database}")
            print(f"Connected to MySQL database: {database}")
        
        return connection, cursor
    
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None, None

def import_csv_to_mysql(csv_dir, host, user, password, database):
    """Import all CSV files in directory to MySQL tables"""
    try:
        # Connect to MySQL
        connection, cursor = connect_mysql(host, user, password, database)
        if not connection:
            return
        
        # Create SQLAlchemy engine for pandas
        engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')
        
        # Get all CSV files
        csv_files = [f for f in os.listdir(csv_dir) if f.endswith('.csv')]
        print(f"Found {len(csv_files)} CSV files to import")
        
        # Process each CSV file
        for csv_file in csv_files:
            table_name = os.path.splitext(csv_file)[0]
            file_path = os.path.join(csv_dir, csv_file)
            
            print(f"\nProcessing {csv_file} -> {table_name}")
            
            try:
                # Read CSV with pandas
                df = pd.read_csv(file_path, low_memory=False)
                
                # Print table info
                print(f"  Columns: {', '.join(df.columns[:5])}{'...' if len(df.columns) > 5 else ''}")
                print(f"  Rows: {len(df)}")
                
                # Create table and import data
                df.to_sql(table_name, engine, if_exists='replace', index=False)
                print(f"  Successfully imported to table: {table_name}")
                
            except Exception as e:
                print(f"  Error importing {csv_file}: {e}")
        
        print("\nImport completed. All CSV files have been imported to MySQL.")
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Import CSV files to MySQL and analyze relationships')
    parser.add_argument('--csv-dir', type=str, required=True, help='Directory containing CSV files')
    parser.add_argument('--host', type=str, default='localhost', help='MySQL host')
    parser.add_argument('--user', type=str, required=True, help='MySQL user')
    parser.add_argument('--password', type=str, required=True, help='MySQL password')
    parser.add_argument('--database', type=str, default='nutrisense', help='MySQL database name') 

    args = parser.parse_args()
    
    import_csv_to_mysql(args.csv_dir, args.host, args.user, args.password, args.database)