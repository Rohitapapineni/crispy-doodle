sp=4
for i in range(1,5):
    x='A'
    for j in range(1,sp):
        print(end=' ')
    for k in range(1,i+1):
        print(x,end=' ')
        x=chr(ord(x)+1)
    x=chr(ord(x)-2)
    for j in range(i,1,-1):
        print(x,end=' ')
        x=chr(ord(x)-1)
    print("\n")
    sp=sp-1
    
