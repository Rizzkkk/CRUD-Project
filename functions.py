import mysql.connector

def create_database_connection():
    """Create and return a connection to the MySQL database."""
    try:
        # Connect to MySQL server
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="group19",
            database="CRUD_APP"
        )
        return db_connection
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")
        return None

def create_record(table, values):
    """Insert a new record into the specified table."""
    try:
        db_connection = create_database_connection()
        if db_connection:
            cursor = db_connection.cursor()
            placeholders = ', '.join(['%s'] * len(values))
            insert_query = f"INSERT INTO {table} VALUES ({placeholders})"
            cursor.execute(insert_query, values)
            db_connection.commit()
            print("Record inserted successfully.")
            cursor.close()
            db_connection.close()
    except mysql.connector.Error as err:
        print(f"Error creating record: {err}")

def read_records(table):
    """Read all records from the specified table."""
    try:
        db_connection = create_database_connection()
        if db_connection:
            cursor = db_connection.cursor()
            select_query = f"SELECT * FROM {table}"
            cursor.execute(select_query)
            records = cursor.fetchall()
            if records:
                for record in records:
                    print(record)
            else:
                print("No records found.")
            cursor.close()
            db_connection.close()
    except mysql.connector.Error as err:
        print(f"Error reading records: {err}")

def update_record(table, key_column, key_value, column_value_pairs):
    """Update a record in the specified table."""
    try:
        db_connection = create_database_connection()
        if db_connection:
            cursor = db_connection.cursor()
            set_values = ', '.join([f"{column} = %s" for column, value in column_value_pairs.items()])
            update_query = f"UPDATE {table} SET {set_values} WHERE {key_column} = %s"
            update_values = [value for _, value in column_value_pairs.items()] + [key_value]
            cursor.execute(update_query, update_values)
            db_connection.commit()
            print("Record updated successfully.")
            cursor.close()
            db_connection.close()
    except mysql.connector.Error as err:
        print(f"Error updating record: {err}")

def delete_record(table, key_column, key_value):
    """Delete a record from the specified table."""
    try:
        db_connection = create_database_connection()
        if db_connection:
            cursor = db_connection.cursor()
            delete_query = f"DELETE FROM {table} WHERE {key_column} = %s"
            cursor.execute(delete_query, (key_value,))
            db_connection.commit()
            print("Record deleted successfully.")
            cursor.close()
            db_connection.close()
    except mysql.connector.Error as err:
        print(f"Error deleting record: {err}")

def main():
    tables = ["PAYROLL", "POSITIONS", "FACULTY", "COORD", "SCHOOL", "DEPT_FAC"]
    
    for table in tables:
        print(f"\nWorking with table: {table}")

        values = tuple(input(f"Enter values for {table} separated by commas: ").split(","))
        create_record(table, values)
        

        key_value = input(f"Enter the value of the key column for update in {table}: ")
        column = input("Enter the column name to update: ")
        new_value = input(f"Enter the new value for {column}: ")
        update_record(table, f"{table.lower()}_no", key_value, {column: new_value})
        

        key_value = input(f"Enter the value of the key column for deletion in {table}: ")
        delete_record(table, f"{table.lower()}_no", key_value)
        

        read_records(table)

if __name__ == "__main__":
    main()
