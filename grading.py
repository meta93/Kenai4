student_name = input("what is your name?")
score = int(input("what is your scores?"))
grade = ""
if score >= 80:
    grade = "A"
elif score >= 70 and score < 80:
    grade = "B"
elif score >= 60 and score < 70:
    grade = "C"
elif score >= 50 and score < 60:
    grade ="D"
else:
    grade = "E"
    print(student_name + "grade of " + grade)
students = {}
students[student_name] = (grade)
print(students)
