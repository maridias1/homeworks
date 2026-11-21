# 1.
n = 5
total = 0

for i in range(1, n + 1):
    total = total + i

print(total)


# 2.
number = 4

while number > 0:
    print(number)
    number = number - 1


# 3.
secret_number = 7

while True:
    guess = int(input("Enter a number: "))
    
    if guess == secret_number:
        print("Congratulations! You guessed it.")
        break
    else:
        print("Wrong guess")


# 4.
total_sum = 0

while True:
    user_input = input("Enter a number: ")
    
    if user_input.lower() == 'sum':
        break
    
    number = float(user_input)
    
    if number > 0:
        total_sum = total_sum + number

print(total_sum)
