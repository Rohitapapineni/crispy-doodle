import mysql.connector as sqltor
db=sqltor.connect(host='localhost',database='newdb',password='root',user='root')
mycursor=db.cursor()
query='select * from Persons;'
mycursor.execute(query)
row=mycursor.fetchall()
while row is not None:
    print(row)
    row=mycursor.fetchall()
db.commit()
