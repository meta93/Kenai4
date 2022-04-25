#Code written by Gideon Boateng
#Creating christmas tree using functions
def Xmastree(n):
    for i in range(n):
        for j in range(n-i):
            print(' ',end =' ')
        for k in range(2 * i +1):
            print('*',end=' ')
        print()

#Use of input anf function call
roww = int(input("ENTER THE NUMBER OF ROWS YOU WANT:"))
Xmastree(roww)
