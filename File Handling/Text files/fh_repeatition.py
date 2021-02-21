f=open(r'paragraph.txt')
d=f.read()
words=d.split(' ')
leng=len(words)
lstdup=[]
for i in range(0,leng):
    c=0
    if words[i] in lstdup:
        continue
    for j in range(0,leng):
        if words[i]==words[j]:
            c+=1
    if c>1:
        lstdup.append(words[i])
print(lstdup)
f.close()





#is=7
#and=2
