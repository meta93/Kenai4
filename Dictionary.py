#Dictionary
Colours ={"Orange":"Blue", "Red":"Grey","Black":"Green"}

#Calling a key
print(Colours['Orange'])

#using get command
theircolor = Colours.get('Red')
print(theircolor)

print("Ash is", theircolor)
Colours["Indigo"] = "Violet"
Colours["Pink"] = "White"
print(Colours)