student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

grade = ""

for student in student_scores:

    if 91 <= student_scores[student] <= 100:
        grade = "Outstanding"
    elif 81 <= student_scores[student] <= 90:
        grade = "Exceeds Expectation"
    elif 71 <= student_scores[student] <= 80:
        grade = "Acceptable"
    else:
        grade = "Fail"

    student_grades[student] = grade

print(student_grades)

