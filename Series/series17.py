n=int(input("enter a number "))
sum=0
a=1
b=2
c=a+b
print(a)
print(b)
print(c)
for i in range(1,n+1):
    a=b
    b=c
    c=a+b
    sum=sum+c
    print(c)
print(sum)
