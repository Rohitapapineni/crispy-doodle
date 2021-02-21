def palindrome(s,n,i):
    if i<=len(s):
        n+=s[-i]
        return palindrome(s,n,i+1)
    if n==s:
        print('palindrome')
    else:
        print('not palindrome')

n=''
i=1
s='madam'
palindrome(s,n,i)

