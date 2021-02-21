x=2
sp=5
for i in range (1,6):
    for k in range (sp,0,-1):
        print(' ',end=' ')
    for j in range (1,x):
        print(j,end=' ')
    print()
    sp=sp-1
    x=x+1
