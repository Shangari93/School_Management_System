import mysql.connector as connector

mysql_variable = connector.connect(
    host="localhost",
    user="root",
    password="Shangari@93",
    # database="Minipython"
)

print(mysql_variable)

cursor = mysql_variable.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS Minipython")
cursor.execute("USE Minipython")
# Create the Student table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Student (
    student_id INT PRIMARY KEY,
    name VARCHAR(100),
    class VARCHAR(10),
    section VARCHAR(10),
    age INT,
    python_mark FLOAT,
    maths_mark FLOAT,
    cs_mark FLOAT,
    database_mark FLOAT
)
""")

# Create the teachers table
cursor.execute("""
CREATE TABLE IF NOT EXISTS teachers (
    teacher_id INT PRIMARY KEY,
    name VARCHAR(100),
    class_teacher VARCHAR(10),
    salary FLOAT,
    age INT,
    experience INT
)
""")

# Create the Principal table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Principal (
    principal_id INT PRIMARY KEY,
    name VARCHAR(100),
    salary FLOAT,
    age INT,
    experience INT
)
""")

# Create the Admin table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Admin (
    admin_id INT PRIMARY KEY,
    admin_password VARCHAR(100)
)
""")

insert_query = """
INSERT INTO Student (student_id, name, class, section, age, python_mark, maths_mark, cs_mark, database_mark)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
"""
student_values = [
    (1111, 'John', '10A', 'A', 16, 90.0, 87.2, 92.0, 85.8),
    (1112, 'Shan', '11A', 'A', 17, 60.0, 95.0, 92.3, 82.8),
    (1113, 'Raj', '11A', 'A', 17, 75.0, 80.0, 96.0, 78.8),
    (1114, 'Roy', '10A', 'A', 16, 92.0, 87.5, 99.0, 58.8),
    (1115, 'Giri', '10A', 'C', 16, 77.0, 77.0, 90.0, 98.8),
    (1116, 'Reddy', '8B', 'D', 14, 90.0, 87.0, 95.0, 97.0)
]
cursor.executemany(insert_query, student_values)
mysql_variable.commit()
print("Students inserted successfully.")

insert_query = """
INSERT INTO teachers (teacher_id, name, class_teacher, salary, age, experience)
VALUES (%s, %s, %s, %s, %s, %s)
"""
teacher_values = [
    (123, 'vidhya', '10A', 65000.0, 55, 10),
    (11, 'raja', '11A', 40000.0, 43, 8),
    (165, 'murugesh', '10A', 35000.0, 35, 7),
    (13, 'selvi', '8B', 35000.0, 35, 7),
    (14, 'gomathy', '11A', 43000.0, 32, 8)
]
cursor.executemany(insert_query, teacher_values)
mysql_variable.commit()
print("Teachers inserted successfully.")

insert_query = """
INSERT INTO Principal (principal_id, name, salary, age, experience)
VALUES (%s, %s, %s, %s, %s)
"""
principal_values = (111, 'Tom', 1000000.0, 45, 20)
cursor.execute(insert_query, principal_values)
mysql_variable.commit()
print("Principal inserted successfully.")

insert_query = """
INSERT INTO Admin (admin_id, admin_password)
VALUES (%s, %s)
"""
admin_values = [
    (1, 'password1'),
    (2, 'password12'),
    (3, 'password123')
]
cursor.executemany(insert_query, admin_values)
mysql_variable.commit()
print("Admin inserted successfully.")

admin_id = input("Enter Admin id: ")
admin_passwd = input("Enter Admin password: ")

cursor_admin = mysql_variable.cursor()
query = "SELECT * FROM Admin"
cursor_admin.execute(query)
output = cursor_admin.fetchall()
admin_enter = False

for row in output:
    db_admin_id = row[0]
    db_passwd = row[1]
    if str(admin_id) == str(db_admin_id) and admin_passwd == db_passwd:
        admin_enter = True
        break

if admin_enter:
    print('He is a valid admin')
    print("Enter 1 for student")
    print("Enter 2 for teacher")
    print("Enter 3 for Principal")
    selected_from_admin = input("Enter a number: ")

    if int(selected_from_admin) == 1:
        print('1 for entering a new student')
        print('2 for updating a student')
        print('3 for deleting a student')
        student_formating = input("Enter your choice for student: ")
        print(student_formating)

        if int(student_formating) == 1:
            print('Enter the following data to insert a student:\nstudent_id, name, class, section, age, python Mark, Maths Mark, CS mark, database mark')
            student_fields = input('Enter the fields as space-separated values: ')
            student_values = tuple(student_fields.split())

            insert_query = """
            INSERT INTO Student (student_id, name, class, section, age, python_mark, maths_mark, cs_mark, database_mark)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(insert_query, student_values)
            mysql_variable.commit()
            print("Student inserted successfully.")

        elif int(student_formating) == 2:
            student_id = input("Enter the student_id to update: ")
            print('Enter the following data to update the student:\nname, class, section, age, python Mark, Maths Mark, CS mark, database mark')
            student_fields = input('Enter the fields as space-separated values: ')
            student_values = tuple(student_fields.split())

            update_query = """UPDATE Student SET name=%s, class=%s, section=%s, age=%s, python_mark=%s, maths_mark=%s, cs_mark=%s, database_mark=%s WHERE student_id=%s
            """
            cursor.execute(update_query, student_values + (student_id,))
            mysql_variable.commit()
            print("Student updated successfully.")

        elif int(student_formating) == 3:
            student_id = input("Enter the student_id to delete: ")
            delete_query = "DELETE FROM Student WHERE student_id=%s"
            cursor.execute(delete_query, (student_id,))
            mysql_variable.commit()
            print("Student deleted successfully.")

    elif int(selected_from_admin) == 2:
        print('1 for entering a new teacher')
        print('2 for updating a teacher')
        print('3 for deleting a teacher')
        teacher_formatin = input("Enter your choice for teacher: ")
        print(teacher_formatin)

        if int(teacher_formatin) == 1:
            print('Enter the following data to insert a teacher:\nteacher_id, name, class_teacher, salary, age, experience')
            teacher_fields = input('Enter the fields as space-separated values: ')
            teacher_values = tuple(teacher_fields.split())

            insert_query = """
            INSERT INTO teachers (teacher_id, name, class_teacher, salary, age, experience)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(insert_query, teacher_values)
            mysql_variable.commit()
            print("Teacher inserted successfully.")

        elif int(teacher_formatin) == 2:
            teacher_id = input("Enter the teacher_id to update: ")
            print('Enter the following data to update the teacher:\nname, class_teacher, salary, age, experience')
            teacher_fields = input('Enter the fields as space-separated values: ')
            teacher_values = tuple(teacher_fields.split())

            update_query = """
            UPDATE teachers SET name=%s, class_teacher=%s, salary=%s, age=%s, experience=%s WHERE teacher_id=%s
            """
            cursor.execute(update_query, teacher_values + (teacher_id,))
            mysql_variable.commit()
            print("Teacher updated successfully.")

        elif int(teacher_formatin) == 3:
            teacher_id = input("Enter the teacher_id to delete: ")
            delete_query = "DELETE FROM teachers WHERE teacher_id=%s"
            cursor.execute(delete_query, (teacher_id,))
            mysql_variable.commit()
            print("Teacher deleted successfully.")

    elif int(selected_from_admin) == 3:
        print('1 for entering a new Principal')
        print('2 for updating a Principal')
        print('3 for deleting a Principal')
        principal_formatin = input("Enter your choice for Principal: ")
        print(principal_formatin)

        if int(principal_formatin) == 1:
            print('Enter the following data to insert a Principal:\nprincipal_id, name, salary, age, experience')
            principal_fields = input('Enter the fields as space-separated values: ')
            principal_values = tuple(principal_fields.split())

            insert_query = """
            INSERT INTO Principal (principal_id, name, salary, age, experience)
            VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(insert_query, principal_values)
            mysql_variable.commit()
            print("Principal inserted successfully.")

        elif int(principal_formatin) == 2:
            principal_id = input("Enter the principal_id to update: ")
            print('Enter the following data to update the Principal:\nname, salary, age, experience')
            principal_fields = input('Enter the fields as space-separated values: ')
            principal_values = tuple(principal_fields.split())

            update_query = """
            UPDATE Principal SET name=%s, salary=%s, age=%s, experience=%s WHERE principal_id=%s
            """
            cursor.execute(update_query, principal_values + (principal_id,))
            mysql_variable.commit()
            print("Principal updated successfully.")

        elif int(principal_formatin) == 3:
            principal_id = input("Enter the principal_id to delete: ")
            delete_query = "DELETE FROM Principal WHERE principal_id=%s"
            cursor.execute(delete_query, (principal_id,))
            mysql_variable.commit()
            print("Principal deleted successfully.")

else:
    print('User ID or password is wrong')

cursor.close()
cursor_admin.close()
mysql_variable.close()