x=int (input (" enter a no. "))
y=int (input (" enter a no. "))
if x>y:
    min=y
else:
    min=x
for i in range (min,1,-1):
    if x%i==0 and y%i==0:
        hcf=i
        break
lcm=x*y/hcf
print (hcf,lcm)
        
