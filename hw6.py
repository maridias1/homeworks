my_dict = {
  "students": [
    {"id": 11, "name": "M", "age": 99},
    {"id": 11, "name": "M", "age": 99},
    {"id": 11, "name": "M", "age": 99},
    {"id": 11, "name": "M", "age": 99},
    {"id": 11, "name": "M", "age": 99},
    {"id": 11, "name": "M", "age": 99}
  ],
"subjects": [
    {"id": 1, "name": "Math", "grades": {"11": "B"}},
    {"id": 2, "name": "Physics", "grades": {"11": "A"}},
    {"id": 3, "name": "English", "grades": {"11": "A"}},
    {"id": 4, "name": "Chemistry", "grades": {"11": "B"}},
    {"id": 5, "name": "History", "grades": {"11": "C"}},
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
