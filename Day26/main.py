import pandas
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

#######################################

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dict)

print(student_data_frame)

for (index, row) in student_data_frame.iterrows():
    ##print(index)
    print(row)
    ##print(row.student)
    ##print(row.score)
