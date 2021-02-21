def factor(n,i):
    if i==n:
        print(n)
    if i<n:
        if n%i==0:
            print(i)
        factor(n,i+1)
n=18
factor(n,1)
