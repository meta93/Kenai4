#list
MyfavouriteFood = [ "Banku", "Fufu"]

#Adding to the list
MyfavouriteFood.append("Rice")
MyfavouriteFood.append("Emena")
print(MyfavouriteFood)

#Inserting to the list to a specific index
MyfavouriteFood.insert(3, "GOB3")
print(MyfavouriteFood)

#Combining two list
Ourfavouritemusic = ["Afrobeats", "Agbaja", "Hiplife","Country"]
MyfavouriteFood.extend(Ourfavouritemusic)
print(MyfavouriteFood)

#Remove an item in a list
Ourfavouritemusic.pop(1)
MyfavouriteFood.remove("Banku")
del MyfavouriteFood[0]
print(MyfavouriteFood)

#listing items in the list
for item in MyfavouriteFood:
    print(item)
print(len(MyfavouriteFood))

#list of numbers
Mynumbers = [2,34,56,89,0,1,35,67]
Mynumbers.sort()
print(Mynumbers)

#Reverse elements in a list
Mynumbers.sort(reverse = True)




