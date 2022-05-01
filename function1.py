def demo(x):
    pi = 3.142
    #this finction calculated the area of a circle
    #x (int) is the radius of the circle
    #y (int) is the area of the circle
    y = pi*x**2
    return y

x = int(input("Please enter the radius of the circle: "))
print(demo(x))