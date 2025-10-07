import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to PyPassword generator!")
let = int(input("How many letters would you like to have in your Password\n"))
num = int(input("How many numbers would you like\n"))
sym= int(input("How many symbols would you like\n"))

password =[]
for letter in range(1 , let + 1):
    password += random.choice(letters)
for number in range(1, num + 1):
    password += random.choice(numbers)
for symbol in range(1, sym + 1):
    password += random.choice(symbols)
random.shuffle(password)
print(password)

password_01 = ""
for char in password:
    password_01 += char
print(f"Your Password is {password_01}")
