f=open(r'paragraph1.txt','r')
k=f.readlines()
new_string=''
for i in k:
    if 'a' not in i.lower():
        new_string+=i
fw=open(r'copied_para1.txt','w')
fw.write(new_string)
fw.close()
