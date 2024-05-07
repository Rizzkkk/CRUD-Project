import mysql.connector
from datetime import datetime

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

def insert_sample_records(cursor):
    """Insert sample records into each table."""
    try:

        faculty_records = [
            (1, 'Ryan', 'Rafael', '1980-01-01', '2005-05-10'),
            (2, 'Smith', 'Jane', '1975-03-15', '2008-09-20'),
            (3, 'Johnson', 'Michael', '1990-07-20', '2010-12-01'),
            (4, 'Williams', 'Emily', '1988-05-08', '2015-03-18'),
            (5, 'Brown', 'Christopher', '1972-11-30', '2000-10-05')
        ]
        insert_faculty_query = "INSERT INTO FACULTY (fac_no, fac_lname, fac_fname, birth_date, hire_date) VALUES (%s, %s, %s, %s, %s)"
        cursor.executemany(insert_faculty_query, faculty_records)


        school_records = [
            ('S001', 'School of Engineering'),
            ('S002', 'School of Business'),
            ('S003', 'School of Medicine'),
            ('S004', 'School of Arts'),
            ('S005', 'School of Science')
        ]
        insert_school_query = "INSERT INTO SCHOOL (school_no, school_name) VALUES (%s, %s)"
        cursor.executemany(insert_school_query, school_records)


        payroll_records = [
            (1, 5000, '2022-01-01', '2022-01-15'),
            (2, 5500, '2022-01-01', '2022-01-15'),
            (3, 6000, '2022-01-01', '2022-01-15'),
            (4, 4800, '2022-01-01', '2022-01-15'),
            (5, 5200, '2022-01-01', '2022-01-15')
        ]
        insert_payroll_query = "INSERT INTO PAYROLL (fac_no, fac_pay, from_date, to_date) VALUES (%s, %s, %s, %s)"
        cursor.executemany(insert_payroll_query, payroll_records)


        positions_records = [
            (1, 'Professor', '2022-01-01', '2022-12-31'),
            (2, 'Assistant Professor', '2022-01-01', '2022-12-31'),
            (3, 'Associate Professor', '2022-01-01', '2022-12-31'),
            (4, 'Lecturer', '2022-01-01', '2022-12-31'),
            (5, 'Researcher', '2022-01-01', '2022-12-31')
        ]
        insert_positions_query = "INSERT INTO POSITIONS (fac_no, pos, from_date, to_date) VALUES (%s, %s, %s, %s)"
        cursor.executemany(insert_positions_query, positions_records)


        coord_records = [
            ('S001', 1, '2022-01-01', '2022-12-31'),
            ('S002', 2, '2022-01-01', '2022-12-31'),
            ('S003', 3, '2022-01-01', '2022-12-31'),
            ('S004', 4, '2022-01-01', '2022-12-31'),
            ('S005', 5, '2022-01-01', '2022-12-31')
        ]
        insert_coord_query = "INSERT INTO COORD (school_no, fac_no, from_date, to_date) VALUES (%s, %s, %s, %s)"
        cursor.executemany(insert_coord_query, coord_records)


        dept_fac_records = [
            (1, 'S001', '2022-01-01', '2022-12-31'),
            (2, 'S002', '2022-01-01', '2022-12-31'),
            (3, 'S003', '2022-01-01', '2022-12-31'),
            (4, 'S004', '2022-01-01', '2022-12-31'),
            (5, 'S005', '2022-01-01', '2022-12-31')
        ]
        insert_dept_fac_query = "INSERT INTO DEPT_FAC (fac_no, school_no, from_date, to_date) VALUES (%s, %s, %s, %s)"
        cursor.executemany(insert_dept_fac_query, dept_fac_records)

        print("Sample records inserted successfully.")
    except mysql.connector.Error as err:
        print(f"Error inserting sample records: {err}")

def main():
    # Create database connection
    db_connection = create_database_connection()

    if db_connection:
        try:
            # Create cursor object
            cursor = db_connection.cursor()

            # Insert sample records
            insert_sample_records(cursor)

            # Commit changes
            db_connection.commit()

            # Close cursor and connection
            cursor.close()
            db_connection.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
    else:
        print("Database connection failed. Exiting...")

if __name__ == "__main__":
    main()
