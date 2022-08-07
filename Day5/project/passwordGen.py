import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

letters_quantity = random.sample(letters, nr_letters)
numbers_quantity = random.sample(numbers, nr_numbers)
symbols_quantity = random.sample(symbols, nr_symbols)

password_string = ""

for value in letters_quantity:
    password_string += value

for value in numbers_quantity:
    password_string += value

for value in symbols_quantity:
    password_string += value

password_shuffle = random.sample(password_string, len(password_string))

password_shuffle_string = ""

for value in password_shuffle:
    password_shuffle_string += value

print(password_shuffle_string)
