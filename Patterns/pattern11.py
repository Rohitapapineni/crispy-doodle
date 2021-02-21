sp=0
x=5
for i in range(1,6):
    for j in range(1,sp+1):
        print(end=' ')
    for k in range(i,6):
        print(k,end=' ')
    print()
    sp=sp+2
    x=x-1
