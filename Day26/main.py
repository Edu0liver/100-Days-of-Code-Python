import random

numbers = [1, 2, 3]

new_list = [n + 1 for n in numbers]
print(new_list)

#######################################

names = ["John", "Bob", "Mosh", "Sarah", "Mary"]

students_score = { student:random.randint(1, 100) for student in names }

print(students_score)

passed_students = { student:score for (student, score) in students_score.items() if score > 70 }

print(passed_students)
