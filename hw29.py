import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="")

cursor = db.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS university_db")
cursor.execute("USE university_db")

cursor.execute("DROP TABLE IF EXISTS students")

cursor.execute(
    """
    CREATE TABLE students (
        studentID INT AUTO_INCREMENT PRIMARY KEY,
        studentFirstName VARCHAR(50),
        studentLastName VARCHAR(50),
        studentAge INT
    )
"""
)

students_data = [
    ("Mari", "Dias", 1),
]

cursor.executemany(
    """
    INSERT INTO students (studentFirstName, studentLastName, studentAge)
    VALUES (%s, %s, %s)
""",
    students_data,
)
db.commit()

cursor.execute(
    """
    SELECT studentLastName, studentFirstName, studentAge 
    FROM students 
    ORDER BY studentLastName ASC, studentFirstName ASC
"""
)

results = cursor.fetchall()

print(f"{'Last Name':<20} {'First Name':<15} {'Age':<5}")
print("-" * 45)
for row in results:
    print(f"{row[0]:<20} {row[1]:<15} {row[2]:<5}")

cursor.close()
db.close()
