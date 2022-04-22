#Using elif
#Declaration of  variables & use of input function
studentname = input("What is the student's name?")
score =int(input("What is their score?"))
grade = str

#use of elif to show the grades
if score >= 80:
    grade = "A"
elif score >= 70 and score < 80:
    grade = "B"
elif score >= 60 and score < 70:
    grade ="C"
elif score >=50 and score < 60:
    grade ="D"
else:
    grade = "E"

#use of print function to display the grade of student
print(studentname +" has a grade of " + grade)

#Use of dictionaries
students = {}
students[studentname] = grade
print(students)

students = {}
students[studentname] = { "score": score,"grade":grade}
print(students)