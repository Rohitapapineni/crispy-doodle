f=open(r'separate_#.txt','r')
str1=f.readlines()
a=0
new_words=''
for line in str1:
    for word in line:
        if word.isspace():
            new_words+='#'
        else:
            new_words+=word
        a+=1
k=open(r'separte_#1.txt','w')
str2=k.write(new_words)
k.close()
f.close()
