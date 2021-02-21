f=open(r'textfile.txt','r')
lines=f.readlines()
list=[]
for line in lines:
    words=line.split()
    for i in words:
        word=i+'#'
        list.append(word)
    print(list)
