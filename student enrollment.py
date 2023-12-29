import json
import mysql.connector
from tkinter import Tk, Label, Entry, Button, messagebox

# MySQL database configuration
db_config = {
    "host": "your_mysql_host",
    "user": "your_mysql_user",
    "password": "your_mysql_password",
    "database": "your_mysql_database"
}

# Create a MySQL connection
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

# Create the STUDENT_TABLE if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS STUDENT_TABLE (
        RollNo INT PRIMARY KEY,
        FullName VARCHAR(255),
        Class VARCHAR(255),
        BirthDate VARCHAR(255),
        Address VARCHAR(255),
        EnrollmentDate VARCHAR(255)
    )
''')
connection.commit()

def submit_form():
    try:
        # Get data from the form
        roll_no = int(entry_roll.get())
        full_name = entry_name.get()
        class_name = entry_class.get()
        birth_date = entry_birth.get()
        address = entry_address.get()
        enrollment_date = entry_enrollment.get()

        # Check if Roll No. already exists in the database
        cursor.execute('SELECT * FROM STUDENT_TABLE WHERE RollNo=%s', (roll_no,))
        existing_student = cursor.fetchone()

        if existing_student:
            messagebox.showerror("Error", "Roll No. already exists!")
            return

        # Insert the new student data into the database
        cursor.execute('''
            INSERT INTO STUDENT_TABLE
            (RollNo, FullName, Class, BirthDate, Address, EnrollmentDate)
            VALUES (%s, %s, %s, %s, %s, %s)
        ''', (roll_no, full_name, class_name, birth_date, address, enrollment_date))

        # Commit the changes
        connection.commit()

        messagebox.showinfo("Success", "Student enrolled successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the GUI
root = Tk()
root.title("Student Enrollment Form")

# Entry fields, labels, and submit button (same as before)

# Run the GUI
root.mainloop()

# Close the database connection when the GUI is closed
connection.close()
