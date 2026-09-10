import mysql.connector

# მონაცემთა ბაზასთან დაკავშირება (XAMPP პარამეტრებით)
db = mysql.connector.connect(host="localhost", user="root", password="")

cursor = db.cursor()

# ბაზის შექმნა და არჩევა
cursor.execute("CREATE DATABASE IF NOT EXISTS university_db")
cursor.execute("USE university_db")

# ცხრილის თავიდან შექმნა (რომ ძველი მონაცემები არ გაორმაგდეს გაშვებისას)
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

# 5 საწყისი სტუდენტი + კოტე კახიძე ერთ სიაში
students_data = [
    ("გრიგოლ", "აბულაძე", 31),
    ("ანა", "გერგაული", 25),
    ("ქეთევან", "კახიძე", 26),
    ("ანდრო", "შალიკაშვილი", 29),
    ("ნინო", "ხარაზიშვილი", 24),
    ("კოტე", "კახიძე", 27),  # დამატებითი სტუდენტი
]

# მონაცემების ბაზაში ჩატვირთვა
cursor.executemany(
    """
    INSERT INTO students (studentFirstName, studentLastName, studentAge)
    VALUES (%s, %s, %s)
""",
    students_data,
)
db.commit()

# მონაცემების წამოღება და ანბანის მიხედვით დალაგება (ჯერ გვარით, შემდეგ სახელით)
cursor.execute(
    """
    SELECT studentLastName, studentFirstName, studentAge 
    FROM students 
    ORDER BY studentLastName ASC, studentFirstName ASC
"""
)

results = cursor.fetchall()

# შედეგების სუფთად დაბეჭდვა ეკრანზე
print(f"{'გვარი':<20} {'სახელი':<15} {'ასაკი':<5}")
print("-" * 45)
for row in results:
  print(f"{row[0]:<20} {row[1]:<15} {row[2]:<5}")

# კავშირის დახურვა
cursor.close()
db.close()