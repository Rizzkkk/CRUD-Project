import http.server
import json
import mysql.connector

# HTTP Server
class MyHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            with open('index.html', 'rb') as file:
                html_content = file.read()

            self.wfile.write(html_content)
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == '/add_employee':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            employee_data = json.loads(post_data)
            add_employee(employee_data)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'message': 'Employee added successfully'}).encode())
        else:
            self.send_response(404)
            self.end_headers()

# Database Functions
def connect_to_database():
    try:
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

def create_tables():
    try:
        db_connection = connect_to_database()
        if db_connection:
            cursor = db_connection.cursor()
            create_employees_table = """
                CREATE TABLE IF NOT EXISTS employees (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    email VARCHAR(255) NOT NULL,
                    phone VARCHAR(15) NOT NULL,
                    address VARCHAR(255) NOT NULL
                )
            """
            cursor.execute(create_employees_table)
            db_connection.commit()
            print("Employees table created successfully.")
            cursor.close()
            db_connection.close()
    except mysql.connector.Error as err:
        print(f"Error creating tables: {err}")

def add_employee(employee_data):
    try:
        db_connection = connect_to_database()
        if db_connection:
            cursor = db_connection.cursor()
            sql = "INSERT INTO employees (name, email, phone, address) VALUES (%s, %s, %s, %s)"
            values = (employee_data['name'], employee_data['email'], employee_data['phone'], employee_data['address'])
            cursor.execute(sql, values)
            db_connection.commit()
            print(f"{cursor.rowcount} record inserted.")
            cursor.close()
            db_connection.close()
    except mysql.connector.Error as err:
        print(f"Error creating record: {err}")

# Sample Data Insertion
def insert_sample_records(cursor):
    """Insert sample records into the employees table."""
    try:
        sql = "INSERT INTO employees (name, email, phone, address) VALUES (%s, %s, %s, %s)"
        values = [
            ("Rafael Harnisch", "rrharnisch@mymail.mapua.edu.ph", "1234567890", "Mapua University"),
            ("John Jester D. Domingo", "jjddomingo@mymail.mapua.edu.ph", "1234567890", "Mapua University"),  
            ("Chesney Kayzle A. Bumakil", "ckabumakil@mymail.mapua.edu.ph", "1234567890", "Mapua University")  
        ]
        cursor.executemany(sql, values)
        print(f"{cursor.rowcount} records inserted into employees table.")
    except mysql.connector.Error as err:
        print(f"Error inserting sample records: {err}")


def main():
    # Create tables
    create_tables()

    # Start HTTP server
    server_address = ('', 8000)
    httpd = http.server.HTTPServer(server_address, MyHTTPRequestHandler)
    print('Server running at http://localhost:8000/')
    httpd.serve_forever()

    # Insert records
    db_connection = connect_to_database()
    if db_connection:
        try:
            cursor = db_connection.cursor()
            insert_sample_records(cursor)
            db_connection.commit()
            cursor.close()
            db_connection.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
    else:
        print("Database connection failed. Exiting...")

if __name__ == "__main__":
    main()
