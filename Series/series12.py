n=int (input ("enter a number "))
x=int (input ("enter a number "))
a=2
sum=0
for i in range (1,n+1):
    fact=1
    for j in range(1,a+1):
        fact=fact*j
    sum=sum+(x**(a/fact))
    a=a+2
print (sum)
