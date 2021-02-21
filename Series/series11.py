n=int (input ("enter a number "))
x=1
sum=1
for i in range (1,n+1):
    de=1
    nu=0
    for j in range(1,x+1):
        nu=nu+j
        de=de*j
    print("Nu:",nu)
    print("De:",de)
    sum=sum+(nu/de)
    x=x+1
print("Sum:",sum)
    
