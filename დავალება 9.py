1. 
int_list = [10, 20, 30, 40]

def damateba(x):
    global int_list
    int_list.append(x)

2.
def sias_jami(sia):
    jami = 0
    for x in sia:
        jami = jami + x
    return jami

# გამოსაძახებელად ასე გამოიყენება:
# chemi_sia = [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10]
# print(sias_jami(chemi_sia))

3.
gl_str = "Global"

def shecvla():
    gl_str = "Local"
    return gl_str

4.
def cifrebi(number):
    if number == 0:
        return 0
    else:
        return (number % 10) + cifrebi(number // 10)
    
5.
    def reverse_str(s):
    if len(s) == 0:
        return s
    else:
        return reverse_str(s[1:]) + s[0] 