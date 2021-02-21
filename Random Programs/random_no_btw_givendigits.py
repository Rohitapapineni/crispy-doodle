import random
n=int(input('Enter number: '))
def number(a,b):
    digit=random.randint(int(a)+1,int(b))
    print(digit)
a=('9'*(n-1))
b='9'*n
number(a,b)
