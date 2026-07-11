1. n = 5

total = 0

for i in range(1, n + 1): # i იქნება ჯერ 1, მერე 2, 3, 4 და ბოლოს 5

    total = total + i

print(total) # დაიბეჭდება: 15



2. number = 4

while number > 0:

    print(number)

    number = number - 1

# დაიბეჭდება:

# 4
# 3
# 2
# 1

3. secret_number = 7

while True:
    # პროგრამა სთხოვს მომხმარებელს რიცხვს
    guess = int(input("შეიყვანეთ რიცხვი: "))
    
    if guess == secret_number:
        print("გილოცავ! შენ გამოიცანი.")
        break  # თუ გამოიცნო, პროგრამა აქ წყდება
    else:
        print("ვერ გამოიცანი")


    4. total_sum = 0

while True:
    user_input = input("შეგვყავს: ")
    
    # ვამოწმებთ, სურს თუ არა მომხმარებელს მუშაობის დასრულება
    if user_input.lower() == 'sum':
        break
    
    # ტექსტი გადაგვყავს რიცხვში
    number = float(user_input)
    
    # ვამოწმებთ, არის თუ არა რიცხვი დადებითი
    if number > 0:
        total_sum = total_sum + number

# ბოლოს ვბეჭდავთ მიღებულ ჯამს
print(total_sum)