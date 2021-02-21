s=0
x=int (input ("enter a number "))
y=int (input ("enter a number "))
for i in range (x,y):
    s=0
    for j in range (1,i):
        if i%j==0:
            s=s+j
    if s==i:
        print (i)
