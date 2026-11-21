# 1.
def fibonacci_sequence(n):
    seq = [0, 1]
    
    if n == 1:
        print([0])
    else:
        while len(seq) < n:
            next_num = seq[-1] + seq[-2]
            seq.append(next_num)
        print(seq)


# 2.
def check_anagram(str1, str2):
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False


# 3.
def factorial(n):
    p = 1
    for x in range(1, n + 1):
        p = p * x
    return p


# 4.
def count_char(s, c):
    n = 0
    for x in s:
        if x == c:
            n = n + 1
    return n
