n=int (input ("enter a no. "))
s=0
x=2
y=4
for i in range (1,n+1):
    s=s+x/y
    print(x,y,end=" ")
    x=x+2
    y=y+2
print (s)
