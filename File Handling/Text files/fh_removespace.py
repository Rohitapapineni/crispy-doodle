f=open(r'Resume.txt','r')
str1=f.read()
s=''
for ch in str1:
    if not ch.isspace():
        s+=ch
k=open(r'resume1.txt','w')
str2=k.write(s)
k.close()
f.close()
