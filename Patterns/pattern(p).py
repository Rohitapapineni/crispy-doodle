x=5
for i in range(1,6):
    for j in range(1,x+1):
        print(j,end=' ')
    for k in range(x-1,0,-1):
        print(k,end=' ')
    print()
    x=x-1
