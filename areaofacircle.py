
def area(r):
    """this function returns the area of a circle
    Args:
      r(int): the radius of a circle
       Returns:
           y (int): the area of a circle"""
    pi= 3.142
    y= pi*r**2
    return y
r=int(input("Enter the radius of the circle you wish to find: "))
print(area(r))