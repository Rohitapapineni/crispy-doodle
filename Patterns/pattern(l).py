sp=1
x=7
for i in range (1,5):
    for j in range (1,sp):
        print(" ",end=" ")
    for k in range (1,x+1):
        print('$',end=" ")
    print()
    sp=sp+1
    x=x-2
