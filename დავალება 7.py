1
user_input1 = input("sheiyvanet mimdevroba: ")
elements1 = user_input1.split()
unique_set = set(elements1)
print(unique_set)

2
user_input2 = input("sheiyvanet mimdevroba: ")
elements2 = user_input2.split()
unique_frozenset = frozenset(elements2)
print(unique_frozenset)

3
set1 = {10, 20, 30}
set2 = {30, 40, 50}
combined_set = set1.union(set2)
result_tuple = tuple(combined_set)
print(result_tuple)

4
user_input4 = input("sheiyvanet ricxvebi: ")
temp_list = []
for x in user_input4.split():
    temp_list.append(int(x))
numbers_tuple = tuple(temp_list)
unique_list = list(set(numbers_tuple))
print(unique_list)

5
students = [("Gega", 24), ("Gaga", 21), ("Goga", 19), ("Giga", 27), ("Gagi", 11)]
for student in students:
    print("Name: " + student[0] + ", Age: " + str(student[1]))

6
users1 = ["Irakli", "Giorgi", "Nona", "Oto"]
users2 = ["Kato", "Levani", "Nino", "Dato", "Irakli", "Nemo"]
intersection = set(users1).intersection(set(users2))
print(list(intersection))