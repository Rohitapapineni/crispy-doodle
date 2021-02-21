import mysql.connector as sqltor
db=sqltor.connect(host='localhost',database='newdb',password='root',user='root')
mycursor=db.cursor()
mycursor.execute("create table EMPLOYEE (empno int(2), name varchar(25), debt varchar(25), salary int(10));")
mycursor.execute("insert into EMPLOYEE values (1,'Amit','sales',25000);")
mycursor.execute("insert into EMPLOYEE values (2,'jitendra','it',60000);")
mycursor.execute("insert into EMPLOYEE values (3,'surendra','it',350000);")
mycursor.execute("insert into EMPLOYEE values (4,'vikas','hr',50000);")
db.commit()
