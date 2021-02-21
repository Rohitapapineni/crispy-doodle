f=open(r'student.txt','r')
name=str(input('Enter name: '))
k=f.readlines()
c=0
for i in range(0,len(k)):
    d=k[i]
    if name==d[0:len(d)-1]:
        c=1
if c==1:
    print('Yes')
else:
    print('no')
f.close()
