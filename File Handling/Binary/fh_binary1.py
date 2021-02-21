import pickle
filename =""
filehand=open(r'student.dat',"wb")
ans='y'
student=[]
while ans=='y':
    name = input('enter a name: ')
    roll = int(input("enter roll: "))
    student.append([name,roll])
    ans=input("do u want to enter more records: ")
pickle.dump(student,filehand)
filehand.close()

student=[]
x=int(input('enter roll number to search: '))
fileread=open(r'student.dat',"rb")
student = pickle.load(fileread)
for data in student:
    if data[1]==x:
        print(data[0])

