s=0
n=153
num=n
while n!=0:
    rem=n%10
    s=s+(rem**3)
    n=n//10
if s==num:
    print(s)
