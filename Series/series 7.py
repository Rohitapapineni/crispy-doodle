n=int (input ("enter a no. "))
x=2
sum=0
for i in range (1,n+1):
    fact=1
    for j in range(1,x+1):
        fact=fact*j
    sum=sum+fact
    x=x+2
print(sum)
