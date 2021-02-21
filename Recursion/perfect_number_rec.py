def perfect_number(n,i,s):
    if i==n:
        if n==s:
            print('Perfect Number')
        else:
            print('not perfect')
    if i<n:
        if n%i==0:
            s+=i
        perfect_number(n,i+1,s)
    
perfect_number(6,1,0)
