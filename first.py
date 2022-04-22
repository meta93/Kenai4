studentname = input('what is the student''s name?')
score = int(input)('what is their score?')
grade = ''
if score >=80:
    grade = 'A'
elif score >= 70 and score < 80:
    grade = 'B'
elif score >= 60 and score < 70:
    grade = 'C'
elif score >= 50 and score < 60:
    grade = 'D'
else:
    grade = 'E'
print(studentname + ' has a grade of ' + grade)




