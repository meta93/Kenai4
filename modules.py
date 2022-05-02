import math

absolute = -5.999
floor_test = 198.42

result1 = math.fabs(absolute)
result2 = math.floor(floor_test)

#print("absolute Value: ", result1)
#print("floor Value: ", result2)

#name = input("What is your name? ")
#color = input("What is your favorite color?  ")
#animal = input("What is your favorite animal?  ")
#print("{}, you like a {} {}!".format(name,color,animal))

myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))

class_roster = ["Xiulan","Kwaku","Shirley"]
test_scores = [86,93,80]
print(class_roster) 
print(test_scores)

class_roster = ["Xiulan","Kwaku","Shirley"] 
test_scores = [86,93,80]
for student in class_roster: 
    print(student)
for score in test_scores: 
    print(score)

myDict = {} 
myDict["one"] = 1 
myDict["two"] = 2 
myDict[3] = "three" 
myDict["four"] = 4.4
print(myDict[3])
for key, value in myDict.items(): 
    print(key, value)