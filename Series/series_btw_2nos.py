a=int(input('Enter first no.:'))
b=int(input('Enter last no.:'))
def series(a,b):
    x=(b-a)/3
    return [a,x+a,2*x+a,b]
print(series(a,b))
        
