from random import randint
import pandas

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

students_scores = {student: randint(1, 100) for student in names}
# print(students_scores)

passed_students = {name: score for (name, score) in students_scores.items() if score > 60}
print(passed_students)

# Loop through pandas dataFrame
students_dict = {
    "student": ["Alex", "Beth", "Caroline"],
    "score": [90, 43, 80]
}

students_df = pandas.DataFrame(students_dict)

for(index, row) in students_df.iterrows():
    print(row)
    print(row.student)
    print(row.score)
