my_dict = {
  "students": [
    {"id": 20, "name": "Giorgi", "age": 25},
    {"id": 25, "name": "Giorgi", "age": 23},
    {"id": 56, "name": "Nika", "age": 25},
    {"id": 100, "name": "Nika", "age": 22},
    {"id": 1232, "name": "Dato", "age": 22},
    {"id": 846723, "name": "Archili", "age": 32}
  ],
  "subjects": [
    {"id": 1, "name": "Math", "grades": {"20": "B", "25": "A", "56": "B", "100": "A", "1232": "C", "846723": "A"}},
    {"id": 2, "name": "Physics", "grades": {"20": "A", "25": "B", "56": "B", "100": "A", "1232": "C", "846723": "B"}},
    {"id": 3, "name": "English", "grades": {"20": "A", "25": "A", "56": "A", "100": "A", "1232": "B", "846723": "A"}},
    {"id": 4, "name": "Chemistry", "grades": {"20": "B", "25": "B", "56": "B", "100": "A", "1232": "A", "846723": "A"}},
    {"id": 5, "name": "History", "grades": {"20": "C", "25": "B", "56": "B", "100": "A", "1232": "A", "846723": "A"}},
  ]
}

ids = []
for student in my_dict["students"]:
    ids.append(str(student["id"]))

print("studentebis ID:", ", ".join(ids))
chosen_id = input("airchiet studentis ID: ")

selected_student = None
for student in my_dict["students"]:
    if str(student["id"]) == chosen_id:
        selected_student = student

if selected_student:
    print("\nstudent infomration:")
    print("ID:", selected_student["id"], "Name:", selected_student["name"], "Age:", selected_student["age"])
    
    for subject in my_dict["subjects"]:
        subject_name = subject["name"]
        grades_dict = subject["grades"]
        if chosen_id in grades_dict:
            print("subject:", subject_name, "grade:", grades_dict[chosen_id])