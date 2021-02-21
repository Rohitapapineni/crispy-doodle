f = open(r'upper_n_lowercase.txt','r')
str1=f.read()
lower=0
upper=0
for ch in str1:
    if ch.islower():
        lower+=1
    elif ch.isupper():
        upper+=1
print("uppercase letters: ",upper)
print("lowercase letters: ",lower)
f.close()
