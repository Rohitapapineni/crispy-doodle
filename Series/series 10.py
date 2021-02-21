n=int (input("enter a number "))
a=10
b=1
c=3
sum=0
for i in range (1,n+1):
    sum=sum + (a*b)/c
    c=c+2
    b=b+2
    a=a+10
print("sum:",sum)

