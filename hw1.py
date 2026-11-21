# 1.
num_list = [44, 23, 11, 8, 20, 56, 33, 55]
number = 56
print(f"Enter a number: {number}")

if number in num_list:
    print("The number in list")
else:
    print("The number not in list")

# 2.
num = 25
print(f"Enter an integer: {num}")

if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

# 3.
st1 = "Hello"
st2 = "Hello"

if st1 is st2:
    print("Same object")
else:
    print("Different object")

# 4.
num_list = [44, 23, 11, 8, 20, 56, 33, 55]
user_num = 40
print(f"Enter a number: {user_num}")

if user_num > num_list[2] and user_num < num_list[-1]:
    print("More than list elements")
elif user_num == num_list[5]:
    print("Equal")
else:
    print("None of the conditions were met")
