import csv
with open(r'Movies.csv','a') as csvfile:
    writer=csv.writer(csvfile,delimiter=',')
    ans='y'
    while ans=='y' or ans=='Y':
        sno=int(input('Enter SNO:'))
        movie_name=input('Enter movie name:')
        actor=input('Enter actor name:')
        ans=input('Do you want to give another input?:')
        writer.writerow([sno,movie_name,actor])
with open(r'Movies.csv','r') as csvfile2:
    reader=csv.reader(csvfile2,delimiter=',')
    for row in reader:
        if row[2].lower()=='salman khan':
            print(row)
