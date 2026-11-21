# 1.
int_list = [10, 20, 30, 40]

def add_element(x):
    global int_list
    int_list.append(x)


# 2.
def sum_list(lst):
    total = 0
    for x in lst:
        total = total + x
    return total


# 3.
gl_str = "Global"

def change_str():
    gl_str = "Local"
    return gl_str


# 4.
def sum_digits(number):
    if number == 0:
        return 0
    else:
        return (number % 10) + sum_digits(number // 10)


# 5.
def reverse_str(s):
    if len(s) == 0:
        return s
    else:
        return reverse_str(s[1:]) + s[0]
