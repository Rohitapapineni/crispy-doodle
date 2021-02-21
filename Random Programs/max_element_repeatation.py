'''string = "grass is greener on the other side"
freq = [None] * len(string)
minChar = string[0]
maxChar = string[0]  
   
#Count each word in given string and store in array freq  
for i in range(0, len(string)):  
    freq[i] = 1
    for j in range(i+1, len(string)):  
        if(string[i] == string[j] and string[i] != ' ' and string[i] != '0'):  
            freq[i] = freq[i] + 1
              
            #Set string[j] to 0 to avoid printing visited character  
            string = string[ : j] + '0' + string[j+1: ]  
              
#Determine minimum and maximum occurring characters  
min = max = freq[0]  
for i in range(0, len(freq)):  
      
    #If min is greater than frequency of a character  
    #then, store frequency in min and corresponding character in minChar  
    if(min > freq[i] and freq[i] != '0'):  
        min = freq[i]
        minChar = string[i] 
    #If max is less than frequency of a character   
    #then, store frequency in max and corresponding character in maxChar  
    if(max < freq[i]):  
        max = freq[i]
        maxChar = string[i] 
   
print("Minimum occurring character: " + minChar)  
print("Maximum occurring character: " + maxChar)
'''
A = [10,12,15,17,20,30]
for i in range(0,6):
    if (A[i] % 2 == 0):
        A[i] /= 2
    elif (A[i] % 3 == 0):
        A[i] /= 3
    elif (A[i] % 5 == 0):
        A[i] /= 5
for i in range(0,6):
    print(A[i],end= "#")
