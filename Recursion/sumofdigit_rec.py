a=0
def sumofdigit(n):
    global a
    s=n%10
    a+=s
    if s==0:
        return a
    return sumofdigit(n//10)
n=1123
print(sumofdigit(n))
