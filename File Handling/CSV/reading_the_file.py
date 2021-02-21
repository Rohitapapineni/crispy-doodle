import csv
f = open('paragraph1.csv')
csv_reader = csv.reader(f, delimiter=',')
line_count = 0
for row in csv_reader:
    print(row)
