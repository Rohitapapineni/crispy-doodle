f=open(r'longestword.txt')
d=f.readline()
ch=d.split()
max=''
for i in range(0,len(ch)):
    max=ch[i]
    maxlen=len(ch[i])
    if maxlen<len(ch[i]):
        max=ch[i]
print(max)
f.close()
    
