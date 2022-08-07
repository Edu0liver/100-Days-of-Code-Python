import math

student_heights = input("Input a list of student heights: ").split(",")
# Format: 180, 124, 165, 173, 189, 169, 146

count = 0
student_heights_total = 0

for student_height in student_heights:
    student_heights_total += int(student_height)
    count += 1

average_student_height = math.floor(student_heights_total / count)

print(f"Average students height: {average_student_height}")
