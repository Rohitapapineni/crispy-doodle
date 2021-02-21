def call_result_add(n1,n2):
    result=int(n1)+int(n2)
    print(result)

def call_result_subtract(n1,n2):
    
    result=int(n1)-int(n2)
    print(result)

def call_result_multiply(n1,n2):
  
    result=int(n1)*int(n2)
    print(result)
def call_result_divide(n1,n2):
    
    result=int(n1)/int(n2)
    print(result)

n1=int(input('Enter 1st number : '))
n2=int(input('Enter 2nd number : '))
operation=input('Enter the operation : ')
if operation=='+':
    call_result_add(n1,n2)
elif operation=='-':
    call_result_subtract(n1,n2)
elif operation=='x' or operation=='*':
    call_result_multiply(n1,n2)
elif operation=='/':
    call_result_divide(n1,n2)
else:
    print('wrong input')
    
