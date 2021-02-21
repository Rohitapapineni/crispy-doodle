def appendlist(list,n):
    list.append(n);
    print(list)
list=[]
a=int(input('Number of elements required in the list:'))
for i in range(0,a):
    x=int(input('Enter element:'))
    list.append(x);
n=int(input('Enter element to append:'))
appendlist(list,n)
