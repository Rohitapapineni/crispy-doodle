x=5
sp=1
for i in range(1,6):
    for k in range(1,sp):
        print(' ',end=" ")
    for j in range(x,0,-1):
        print(j,end=' ')
    for l in range(1,x+1):
        print(l,end=' ')
    print()
    sp=sp+1
    x=x-1
