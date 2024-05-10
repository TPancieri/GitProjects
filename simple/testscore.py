student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99, 
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

def assign_grade(score):
    grade_map = {
        (91, 101): "Outstanding",
        (81, 91): "Exceeds Expectations",
        (71, 81): "Acceptable",
        (0, 71): "Fail",
    }
    for score_range, grade in grade_map.items():
        if score_range[0] <= score < score_range[1]:
            return grade

for student, score in student_scores.items():
    grade = assign_grade(score)
    student_grades[student] = grade

print(student_grades)