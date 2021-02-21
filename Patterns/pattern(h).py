x='A'
for i in range (5,0,-1):
    print()
    x='A'
    for j in range (1,i+1):
        print(x,end=' ')
        x=chr(ord(x)+1)   

#x = chr(ord(ch) + 3) 
