def rev_str(s):
    if len(s)==0:
        return s
    return rev_str(s[1:])+s[0]
s='abc'
print(rev_str(s))
