x=int (input (" enter marks "))
max=x
min=x
for i in range (1,5):
    x=int (input (" enter marks "))
    if x>max:
        max=x
    if x<min:
        min=x
print (max-min)
