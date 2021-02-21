def maxlist(list):
    print(n)
    max=0
    for i in range(0,n):
        max=list[i]
        if max<list[i]:
            max=list[i]
    print(max)
list=[]
n=int(input('Number of elements required in the list:'))
for i in range(0,n):
    x=int(input('Enter element:'))
    list.append(x);

maxlist(list)
