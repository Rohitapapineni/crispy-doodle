n=int (input("enter a number "))
sum=0
y=0
x=1
for i in range (1,n+1):
    x=x+y
    y=y+2
    print(x)
    sum=sum+x
print(sum)
