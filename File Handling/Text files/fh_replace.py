f=open(r'paragraph.txt','r')
k=f.read()
new_string=''
words=k.split('')
for word in words:
    if word=='30':
        new_word+='25'
    else:
        new_word+=word
    new_word+=' '
fw=open(r'copied_para.txt','w')
fw.write(new_string)
fw.close()
