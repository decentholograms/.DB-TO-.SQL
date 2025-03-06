import sqlite3
import os

def export_db_to_sql(db_path, output_sql_path):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        with open(output_sql_path, 'w', encoding='utf-8') as sql_file:
            for line in conn.iterdump():
                sql_file.write(f'{line}\n')

        print(f"Database successfully exported to {output_sql_path}")
    except Exception as e:
        print(f"Error exporting the database: {e}")
    finally:
        if conn:
            conn.close()

os.system('cls' if os.name == 'nt' else 'clear')

db_name = input("Enter the .db file name (without extension): ")
output_sql_name = input("Enter the output .sql file name (without extension): ")

db_path = db_name + '.db' if os.path.isabs(db_name) else os.path.join(os.getcwd(), db_name + '.db')
output_sql_path = os.path.join(os.getcwd(), output_sql_name + '.sql')

if not os.path.isfile(db_path):
    print(f"Error: The file '{db_name}.db' does not exist in the current directory or the provided path.")
else:
    export_db_to_sql(db_path, output_sql_path)
