"""
in this programe we wnat to print that pattern 
*
**
***
****
*****
"""
n = int(input("enter the number of rows"))
for i in range(1, 6):
    for j in range(1, 6):
        if j <= i:
            print("*", end='')
    else:
        print(" ", end='')
    print()
    """
The above pattern also print in While loop also
coding of While loop
    n=int(input("enter the number of rows"))
row=0
while row<n:
    star=row+1
    while star>0:
        print("*",end='')
        star=star-1
    row=row+1
    print()
    """
