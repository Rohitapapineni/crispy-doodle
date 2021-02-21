f=open(r'count_of_characters.txt','r')
characters=f.read()
lc,uc,vc,cc=0
vowels=['a','e','i','o','u']
for ch in characters:
    if ch.islower():
        lc+=1
    elif ch.isupper():
        uc+=1
    elif ch.isalpha():
        if ch.lower() in vowels:
            vc+=1
        else:
            cc+=1
print('Vowel Count - ',vc)
print('Consonants count - ',cc)
print('Lowercase count - ',lc)
print('Uppercase count - ',uc)
f.close()
