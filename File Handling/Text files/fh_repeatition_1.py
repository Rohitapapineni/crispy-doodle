f=open(r'paragraph.txt')
d=f.read()
words=d.split(' ')
leng=len(words)
lstdup=[]
count=0
for word in words:
    if count(word) in words:
        print(count,word)
f.close()
