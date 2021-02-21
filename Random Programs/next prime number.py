x=int(input("Enter a number:"))
i=x+1
count=0
while i>x:
    count=0
    for j in range(1,i+1):
        if i%j == 0:
            count=count+1
    if count==2:
        print(j)
        break
    i=i+1
