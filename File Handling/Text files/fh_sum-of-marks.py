f=open(r'marks.txt','r')
c=0
#lines=f.readlines()
str=" "
while str:
    str=f.readline()
    list=str.split(' ')
    print(list)
    if list[-1].isalphanum():
        
    #c+=float(list[-1])
    
print('Total Marks:',c)
