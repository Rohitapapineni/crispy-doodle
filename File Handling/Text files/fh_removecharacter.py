f=open(r'file.txt','r')
nf=open(r'new_file.txt','w')
lines=f.readlines()
#words=k.split(' ')
new_line=''
for line in lines:
    if 'a' not in line:
        new_line=line
    nf.write(new_line)
nf.close()
