def circular_lists(l1,l2):
    newlist=l1*2
    n=0
    for i in range(len(newlist)):
        if l2==newlist[i:i+len(l2)]:
            n+=1
    if n>=1:
        print('true')
    else:
        print('false')
l1=[3,4,5,2,6]
l2=[5,2,7,3,4]
circular_lists(l1,l2)
