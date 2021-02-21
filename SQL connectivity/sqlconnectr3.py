import mysql.connector as sqltor
db=sqltor.connect(host='localhost',database='newdb',password='root',user='root')
mycursor=db.cursor()
query="update CLUB set pay=pay+100 where sports = 'Swimming';"
mycursor.execute(query)
row=mycursor.fetchone()
while row is not None:
    print(row)
    row=mycursor.fetchone()
db.commit()
