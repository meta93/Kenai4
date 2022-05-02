from turtle import up


var = "Double Value" 
sumvalue = var + str(4)

def dosomething(valuetocheck): 
    if valuetocheck > 4: 
        print("Bad indent")

# Ask the user for a value and confirm the supplied value is greater than 0
def checkvalue(valuetocheck): 
    assert (type(valuetocheck) is int), "You must enter a number."
    assert (valuetocheck > 0), "Value entered must be greater than 0" 
    if valuetocheck > 4: 
        print("Value is greater than 4")
var = int(input("Enter a number greater than 0: "))
checkvalue(var)