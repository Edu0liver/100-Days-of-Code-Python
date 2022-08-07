
total = input("What what the total bill? ")
percentageTip = input("What percentage tip would you like to give? ")
people = input("How many people to split the bill? ")

floatTotal = float(total)
intPercentageTip = int(percentageTip)
intPeople = int(people)

eachPayment = (((floatTotal / 100) * intPercentageTip) + floatTotal) / intPeople

print(f"Each person should pay {eachPayment}")