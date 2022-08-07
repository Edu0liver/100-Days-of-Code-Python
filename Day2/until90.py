
age = input("Type your age: ")

currentAge = int(age)

years = currentAge
months = currentAge * 12
weeks = currentAge * 52
days = currentAge * 365

years90 = 90
months90 = 90 * 12
weeks90 = 90 * 52
days90 = 90 * 365

yearsDif = years90 - years
monthsDif = months90 - months
weeksDif = weeks90 - weeks
daysDif = days90 - days

print(f"years: {yearsDif}\nmonths: {monthsDif}\nweeks: {weeksDif}\ndays: {daysDif}\n")