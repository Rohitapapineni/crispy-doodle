import csv
total_marks=0
new_list=[]
with open('sample.csv','r') as csvfile:
    csv_reader=csv.reader(csvfile,delimiter=',')
    for row in csv_reader:
        total_marks=int(row[1])+int(row[2])
        row.append(total_marks)
        new_list.append(row)
with open('sample1.csv','w') as csvfile2:
    csv_writer=csv.writer(csvfile2,delimiter=',')
    csv_writer.writerows(new_list)
    
                
