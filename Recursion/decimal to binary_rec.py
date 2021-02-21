s=''
def conversion(n):
    global s
    if n<2:
        return s
    else:
        s+=str(n%2)
        return conversion(n//2)

n=345

print(conversion(n))
