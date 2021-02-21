s=input('enter sentence:')
len=len(s)
a=0
ss=''
while a<len:
    if a==0:
        ss+=s[0].upper()
        a+=1
    elif s[a].isspace() and s[a+1]!='':
        ss+=s[a]
        ss+=s[a+1].upper()
        a+=2
    else:
        ss+=s[a]
        a+=1
print(ss)
    
