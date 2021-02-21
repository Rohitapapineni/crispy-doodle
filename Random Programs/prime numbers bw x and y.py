x=int (input("enter a no. "))
y=int (input("enter a no. "))
for i in range (x,y+1):
    n=i
    count = 0
    for j in range (1,n+1):
        if (n%j==0):
            count=count+1
    if count == 2:
        print (j)


        
