n=int (input ("enter a no. "))
s=0
x=1
for i in range (1,n+1):
   s=i*x
   x=x+1
   s=s+i*x
print (s)
