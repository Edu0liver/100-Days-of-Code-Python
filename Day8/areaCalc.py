import math

def paint_calc(height, width, cover):
    return (height * width) / cover

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

result = math.ceil(paint_calc(test_h, test_w, coverage))

print(f"You will need {result} cans of paint.")
