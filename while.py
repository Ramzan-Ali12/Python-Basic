"""
i = 0
a = 'somepeoplearegood'
while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1
        continue
    print('Current Letter :', a[i])
    i += 1
    """
"""
i = 10
while i < 50:
    j = i-1
    print(j)
    if i == 3:
        continue
print("Thank you")
"""
"""
n = int(input("enter how many rows you want to enter\n"))
for i in range(n):
    for j in range(n):
        if j >= 6-i:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()
    """
"""
n=int(input("enter how many rows you want to enter\n"))
row=0
while row<n:
    space=n-row-1
    while space>0:
        print(end=" ")
        space=space-1
    star=row+1
    while star>0:
        print("*",end=" ")
        star=star-1
    row=row+1
    print()
    """

"""
def pyramid(rows):
    for i in range(rows):
        print(''*(rows - i - 1) + '*'*(i + 1))


pyramid(5)
"""
"""
for row in range(0, 5):
    for col in range(0,5):
        if row + col == 2 or col - row == 2 or row - col == 2 or row + col == 6:
            print("*", end="")
        else:
            print(end=" ")
    print()
    """
for row in range(5):
    for col in range(5):
        if col == 0 or row == 4 or row == col:
            print("*", end="")
        else:
            print(end=" ")
    print() 
