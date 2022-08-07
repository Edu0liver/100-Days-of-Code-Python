import random

names_string = input("Give me everybody's names, separated by a comma. ")
# Example Input: Angela, Ben, Jenny, Michael, Chloe

names = names_string.split(", ")

amount_people = len(names);

index = random.randint(1, amount_people)

who_will_pay = names[index]

print(f"{who_will_pay} will pay!")
