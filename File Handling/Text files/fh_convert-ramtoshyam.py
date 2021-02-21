f=open(r'ramtoshyam.txt','r')
d=f.read()
nf=''
ch=d.split()
leng=len(ch)
for i in range(0,leng):
    if ch[i]=='ram':
        nf+='shyam'
    else:
        nf+=ch[i]
    nf+=' '
wf=open(r'sample.txt','w')
wf.write(nf)
wf.close()
print(nf)
