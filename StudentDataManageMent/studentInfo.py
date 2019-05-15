# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 15:05:05 2019

@author: Subodh
"""

import os
import platform
import mysql.connector

mydb=mysql.connector.connect(host='localhost',user='root',database='sample',passwd='subodh9807')
mycursor=mydb.cursor()
def manageStudent():
    print("""     ==========================================================
             ||                       STUDENT MANAGER                 || 
             ||                                                       || 
            ===========================================================  
        1.To view student info::
        2.To add new student::
        3.To search a particular student::
        4.To remove a student::    
      
           """)
    
    try:
        userInput=int(input("Enter your choice::"))    
    except ValueError:
        if userInput not in range(1,5):
           print("\n For this value there is not any entry.\n")
        else:
           print("\n")
   #creating the table for student data     
    sql1="""CREATE TABLE IF NOT EXISTS student1 (
       `stuid` INT UNSIGNED NOT NULL,
       `stuname` VARCHAR(45) NOT NULL,
       `stuadd` VARCHAR(45) NULL,
       `stumob` VARCHAR(45) NULL,
       `courseapplied` VARCHAR(45) NULL,
       PRIMARY KEY (`stuid`));"""

    mycursor.execute(sql1)
    if userInput==1:
       print("The List of students is::\n")
       sql2="select stuname from student1"
       mycursor.execute(sql2)
       stuName=mycursor.fetchall()
       for student in stuName:
          print(student)
          print("\n")


    elif userInput==2:
        print("Enter the sudent info to be added::")
        Id=int(input("StuId=>"))
        Name=input('Name=>')
        Add=input('Address=>')
        Mob=input('MobileNo=>')
        CourseAp=input('Course Applied=>')
        data_entry={'stuid':Id,'stuname':Name,'stuadd':Add,'stumob':Mob,'courseapplied':CourseAp}
    
        sql3=("INSERT INTO student1"
               "(`stuid`,`stuname`,`stuadd`,`stumob`,`courseapplied`)"
               "VALUES(%(stuid)s,%(stuname)s,%(stuadd)s,%(stumob)s,%(courseapplied)s)")
    
        mycursor.execute(sql3,data_entry)
        mydb.commit()
    
    elif userInput==3:
         print("Enter the name to be searched::")
     
         Name1=input()
         data={'stuname':Name1}
         sql4=("SELECT* FROM student1 WHERE stuname =%(stuname)s")
        
         mycursor.execute(sql4,data)
         Search=mycursor.fetchone()
         print(Search) 
         print("\n")
    elif userInput==4:
         print("Enter the name of student to be removed::")
         Name2=input()
         sql5="delete from student1 where stuname=%(stuname)s"
         mycursor.execute(sql5,{'stuname':Name2})
         mydb.commit()        
         print(Name2+' has removed.\n')
    

#mydb.close()     
manageStudent() 
def runAgain(): #Making Runable Problem1353
	runAgn = input("\nWant To Run Again Y/n: ")
	if(runAgn.lower() == 'y'):
		if(platform.system() == "Windows"): #Checking User OS For Clearing The Screen
			print(os.system('cls')) 
		else:
			print(os.system('clear'))
		manageStudent()
		runAgain()
	else:
		exit() #Print GoodBye Message And Exit The Program

runAgain()
    
    
    
    
    
    
    
    
    
    
    
    
            












       
