count=0
def prime(n,i):
    global count
    if i==0:
        return n
    
    else:
        if n%i==0:
            count+=1
        prime(n,i-1)
    if count==2:
        print('Prime')
        
    else:
        print('Not prime')
        
n=7
prime(n,n)

