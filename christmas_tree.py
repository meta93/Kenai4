def triangle(height):
    stars = 1
    for i in range(height):
        print((' ' * (height-i)) + ('*' * stars))
        stars += 2
        
def treeShape(height):
    pole = 1
    for p in range(height):
        print((' ' * height) + '|')
        
    
height = int(input('Enter the height of the tree: '))
triangle(height)
triangle(height)
triangle(height)
treeShape(height)














