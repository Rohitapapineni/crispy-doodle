count=0
def countofdigits(n):
    global count
    s=n%10
    count+=1
    if s==0:
        return count-1
    return countofdigits(n//10)
n=1124
c=countofdigits(n)
print(c)
