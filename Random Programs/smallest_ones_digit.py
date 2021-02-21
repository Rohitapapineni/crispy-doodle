a=int(input('Enter no.:'))
b=int(input('Enter no.:'))
def number(a,b):
    x=str(a)
    y=str(b)
    if x[-1]<y[-1]:
        print(x)
    elif x[-1]>y[-1]:
        print(y)
    else:
        print(x,y)
number(a,b)
