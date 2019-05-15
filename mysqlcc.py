import mysql.connector as sqlconn
mydb=sqlconn.connect(host='localhost',user="root",passwd='subodh9807')
mycursor=mydb.cursor()
mycursor.execute('show databases')
for i in mycursor:
	print(i)