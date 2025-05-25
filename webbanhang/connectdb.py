import mysql.connector
db=mysql.connector.connect(user='root', password='123456', host='localhost')
code="CREATE DATABASE 'TEST1' "
#RUN
mycursor=db.cursor()
mycursor.execute(code)