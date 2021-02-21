f=open(r'names.txt','r')
lines=f.readlines()
for name in lines:
    if name[0]=='A' or name[0]=='a':
        print(name)
