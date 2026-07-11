1. ჩემი_სია = []

while True:
    ბრძანება = input()

    if ბრძანება == 'a':
        რიცხვი = int(input())
        ჩემი_სია.append(რიცხვი)
        print(ჩემი_სია)
    elif ბრძანება == 'r':
        რიცხვი = int(input())
        if რიცხვი in ჩემი_სია:
            ჩემი_სია.remove(რიცხვი)
        print(ჩემი_სია)
    elif ბრძანება == 'e':
        print(ჩემი_სია)
        break

    2. my_list_1 = [43, '22', 12, 66, 210, ["hi"]]

print(my_list_1.index(210))

my_list_1[-1].append("hello")

del my_list_1[2]
print(my_list_1)

my_list_2 = my_list_1.copy()
my_list_2.clear()

print(my_list_1)
print(my_list_2)

3. import re

ნომერი = input()
შაბლონი = r"^\(\d{3}\) \d{3}-\d{3}$"

if re.fullmatch(შაბლონი, ნომერი):
    print(ნომერი)
else:
    print("Invalid format")

    4. import string

text = input()

has_letter = False
has_digit = False
has_forbidden = False

allowed_chars = string.ascii_letters + string.digits

for char in text:
    if char in string.ascii_letters:
        has_letter = True
    if char in string.digits:
        has_digit = True
    if char not in allowed_chars:
        has_forbidden = True

if has_letter and has_digit and not has_forbidden:
    print("Valid")
else:
    print("Invalid")

    5. text = input()

bytes_data = text.encode('utf-8')
print(bytes_data)

original_text = bytes_data.decode('utf-8')
print(original_text)