print(" Here is my dairy: \n")
f1 = open("files/dairy.txt", "r")
print(f1.read())
f1.close()

print("\n Now lets create another dairy !")
f2 = open("files/dairy2.txt", "w") #THIS CREATES dairy2.txt 
f2.write("Writing in my dairy file!") #THIS WRITES IN dairy2.txt
f2.close()