"""
*****
****
***
**
*    
"""
"""
n = int(input("enter the number of rows "))
for i in range(1, 6): #this loop for rows
    for j in range(1, 6):#this loop for column
        if j>=i:
         print("*",end='')
    else:
       print(" ",end='')
    print()
"""
"""
#The above pattern also print in While loop coding
n=int(input("enter the number of rows"))
row=0
while row>=n:
    while star>=row:
        star=star-1
        while row<=star:
            """