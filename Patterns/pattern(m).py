sp=0
x=5
for i in range(1,6):
    for j in range (1,x+1):
        print(j,end=' ')
    for k in range(1,sp+1):
        print(end=' ')
    for l in range(x,0,-1):
        print(l,end=" ")
    print()
    sp=sp+4
    x=x-1
