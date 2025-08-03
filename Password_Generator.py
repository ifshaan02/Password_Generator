#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

letter_random = []
for letter in range(0,nr_letters):
    letter_random.append(random.choice(letters))

letter_random = ''.join(str(i) for i in letter_random)

symbol_random = []
for symbol in range(0,nr_symbols):
    symbol_random.append(random.choice(symbols))
symbol_random = ''.join(str(i) for i in symbol_random)

number_random = []
for number in range(0,nr_numbers):
    number_random.append(random.choice(numbers))
number_random = ''.join(str(i) for i in number_random)

password_letters = letter_random + symbol_random + number_random


password = ''.join(random.sample(password_letters,len(password_letters)))

print(password)




