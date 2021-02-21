import mysql.connector as sqltor
db=sqltor.connect(host='localhost',database='newdb',password='root',user='root')
mycursor=db.cursor()
query="select * from CLUB order by coachname;"
data=mycursor.execute(query)
row=mycursor.fetchone()
while row is not None:
    print(row)
    row=mycursor.fetchone()
db.commit()
