sp=1
x=5
for i in range(1,6):
    for j in range(1,sp):
        print(' ',end=' ')
    for l in range(x,0,-1):
        print(l,end=' ')
    print()
    sp=sp+1
    x=x-1
