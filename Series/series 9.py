n=int (input ("enter a number "))
a=float(1)
b=1
x=2
sum= 0
for i in range (1,n+1):
    fact=1
    for j in range (1,x+1):
        fact=fact*j
    sum=float(sum+b/fact)
    x=x+2
    b=b+2
print (sum)
