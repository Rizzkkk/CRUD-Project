import mysql.connector

# Function to connect to the MySQL database
def connect_to_database():
    try:
        db_connection = mysql.connector.connect(
            host="localhost",
            user="your_username",
            password="your_password",
            database="crud_app"
        )
        return db_connection
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")
        return None

# Function to create a record in a specified table
def create_record(table, values):
    try:
        db_connection = connect_to_database()
        if db_connection:
            cursor = db_connection.cursor()
            sql = f"INSERT INTO {table} VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, values)
            db_connection.commit()
            print(f"{cursor.rowcount} record inserted.")
            cursor.close()
            db_connection.close()
    except mysql.connector.Error as err:
        print(f"Error creating record: {err}")

# Function to read records from a specified table
def read_records(table):
    try:
        db_connection = connect_to_database()
        if db_connection:
            cursor = db_connection.cursor()
            cursor.execute(f"SELECT * FROM {table}")
            records = cursor.fetchall()
            for record in records:
                print(record)
            cursor.close()
            db_connection.close()
    except mysql.connector.Error as err:
        print(f"Error reading records: {err}")

# Function to delete records from a specified table based on a condition
def delete_record(table, condition):
    try:
        db_connection = connect_to_database()
        if db_connection:
            cursor = db_connection.cursor()
            sql = f"DELETE FROM {table} WHERE {condition}"
            cursor.execute(sql)
            db_connection.commit()
            print(f"{cursor.rowcount} record(s) deleted.")
            cursor.close()
            db_connection.close()
    except mysql.connector.Error as err:
        print(f"Error deleting record: {err}")

# Function to update records in a specified table based on a condition
def update_record(table, new_value, condition):
    try:
        db_connection = connect_to_database()
        if db_connection:
            cursor = db_connection.cursor()
            sql = f"UPDATE {table} SET address = %s WHERE {condition}"
            cursor.execute(sql, (new_value,))
            db_connection.commit()
            print(f"{cursor.rowcount} record(s) affected.")
            cursor.close()
            db_connection.close()
    except mysql.connector.Error as err:
        print(f"Error updating record: {err}")

