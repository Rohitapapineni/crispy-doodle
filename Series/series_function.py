def factorial(a):
    fact=1
    for i in range(a,0,-1):
        fact*=i
    return fact

def power(x,y):
    b=x**y
    return b

n=int(input ("enter a number "))
x=int(input ("enter a number "))
a=2
sum=0.0
for i in range (1,n+1):
    f=factorial(a)
    p=power(x,a)
    sum=sum+(p/f)
    a=a+2
print (sum)



