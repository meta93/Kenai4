def demo(x):
    """This function returns the area of a circle
    Args:
    x (int): the radius of the circle
    Returns:
    y (int): the area of the circle"""
    pi=3.142
    y = pi*x**2
    return y
value = int(input("Enter the radius of the circle:"))
print(demo(value))