n=int(input('enter number of values:'))
li=[]
for i in range(1,n+1):
    s=int(input('enter a number:'))
    li.append(s);
for i in range(0,len(li)):
    for j in range(0,len(li)-1-i):
        if(li[j]>li[j+1]):
            temp=li[j]
            li[j]=li[j+1]
            li[j+1]=temp
print(li)        
