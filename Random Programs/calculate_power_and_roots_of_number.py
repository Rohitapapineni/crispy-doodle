def power(n1,n2):
    result=n1**n2
    print(result)
def root(n1):
    result=n1**(1/2)
    print(result)
msg='''
1.For finding the square root of a number
2.For finding the powers
'''
print(msg)

func=int(input('Enter ur operation : '))
if func==1:
    n1=float(input('Enter the number:'))
    root(n1)
elif func==2:
    n1=float(input('Enter the base number : '))
    n2=float(input('Enter the power : '))
    power(n1,n2)
    
