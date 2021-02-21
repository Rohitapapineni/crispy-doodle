x=int (input ("enter a no."))
for i in range (2,x):
    if x%i==0:
        print(i)
        break
for f in range (x-1,1,-1):
    if x%f==0:
        print(f)
        break
