neg=0
pos=0
while True:
    x=int (input ("enter a number "))
    if x==0:
        break
    if x<0:
        neg=neg+1
    else:
        pos=pos+1
print (neg)
print (pos)
