x=int (input (" enter a no. "))
s=0
for i in range (1,x):
    if x%i==0:
        s=s+i
if s==x:
    print (" its a perfect number ")
else:
    print (" its not a perfect no. ")
    
            
