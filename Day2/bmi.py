
height = input("Type your height(meters) : ")
weight = input("Type your weight(kg) : ")

bmi = int(weight) / float(height) ** 2

strBMI = str(bmi)

print("Your BMI is " + strBMI)