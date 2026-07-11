1. text = input()
encoded_text = text.encode('utf-8')
print(encoded_text)

2. text = input()
text = text.strip()
text = text.lower()
text = text.replace("python", "Python")
text = text + "Python"
print(text)

3.text = input()
length = len(text)
half = int(length / 2)
result = text[0:half]
print(result)

4. import string

text = input()

has_letter = False
has_digit = False
has_bad_char = False

for char in text:
    if char in string.ascii_letters:
        has_letter = True
    elif char in string.digits:
        has_digit = True
    else:
        has_bad_char = True

if has_letter == True and has_digit == True and has_bad_char == False:
    print("Valid")
else:
    print("Invalid")

    5. text = input()
bytes_data = text.encode('utf-8')
print(bytes_data)
new_text = bytes_data.decode('utf-8')
print(new_text)