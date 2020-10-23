#  Importing PYMYSQL And Establishing Connecction With MYSQL

import pymysql
conn=pymysql.connect(host="localhost",user="root",password="",port = 3308)
sql=conn.cursor()

#  Importing Colorama Package
 
from colorama import init
init()

# Importing Shedule(.py File) and Sheduler(Function)

from Shedule import Sheduler

import csv

# Importing OS Module 

import os

# Checking Whether The Folder Are Created If Not Folder will Be Created

def Main():

    if os.path.exists("D://Big-Ben"):
        pass

    else:
        os.mkdir("D://Big-Ben")


    if os.path.exists("D://Big-Ben//Teachers"):
        pass

    else:
        os.mkdir("D://Big-Ben//Teachers")


    if os.path.exists("D://Big-Ben//Class"):

        pass

    else:
        os.mkdir("D://Big-Ben//Class")


    # Creation Of DataBase 

    sql.execute("show databases;")
    data= sql.fetchall()

    for i in data:

        if i[0] == "big_ben":
            sql.execute("use big_ben;")
            break

        else :
            sql.execute("create database big_ben;") 
            sql.execute("use big_ben;")
            break

    # Recieving Input From Admin

    print("\033[2J")
    print("")
    print("")
    print("                       Big Ben")
    print("")
    print("")
    
    Sector = input("SECTOR : ").upper()
    print("")

    standard = int(input("STANDARAD : "))
    print("")

    # Creating Folder For Sector

    if os.path.exists(f"D://Big-Ben//Teachers//{Sector}"):
        pass

    else:
        os.mkdir(f"D://Big-Ben//Teachers//{Sector}")

    if os.path.exists(f"D://Big-Ben//Class{Sector}"):
        pass

    else:
        os.mkdir(f"D://Big-Ben//Class//{Sector}")

    # To Find The Existence Of Tables 

    Reshedule = False
    Find = True
    sql.execute("show tables")
    data = sql.fetchall()

    for i in data:

        if i[0] == "class_" + str(standard):
            print(f"The Time Table for class_{standard} was Already Created ")
            Find = False
            descision = input("Do You Want to Reshedule It! ? Yes / No  : ")
            descision = descision.lower()

            if descision == "yes" :
                Reshedule = True
                Sheduler(standard,conn,Reshedule,Sector) 

            else :
                print("Thank You For Using Big Ben")
            
    if Find:

        noOfSubject = int(input("No . Of . Subject : "))

        print("")

        noOfSection = int(input("No . Of. Section : "))

        # Assining Name Of Section

        listOfSecetion = []

        for i in range(noOfSection):

            alphabet = "Section_" + chr( i + 65)
            listOfSecetion.append(alphabet)

        # Recieving Name Of The Subject From Admin

        listOfSubject = []

        print("\033[2J")
        print("")
        print("")
        print("                       Big Ben")
        print("")
        print("")
        print("Please Enter The Name Of Subjects")

        for i in range(noOfSubject):
            print('')
            subject = input(f"Name Of Subject {i + 1} : ").upper()
            listOfSubject.append(subject)

        # Recieving No Of Periods per Week for Each Subject From Admin

        list_Of_No_Of_Periods = []

        print("\033[2J")
        print("")
        print("")
        print("                       Big Ben")
        print("")
        print("")
        print("Please Enter The No of Periods Per Week For The Following Subject ")

        for i in listOfSubject:
            print("")
            noOfPeriod = int(input(f"{i} : "))
            list_Of_No_Of_Periods.append(noOfPeriod) 

        #  Recieving Class Info

        classInfo = []

        for i in listOfSubject :
            print("\033[2J")
            print("")
            print("")
            print("                       Big Ben")
            print("")
            print("")
            print (f"Please Enter The  Name Of ' {i} ' Teacher For The Following Section ")

            # Appending Name Of Subject And NoOf Periods 

            nameOfTeachers = []
            nameOfTeachers.append(i)
            nameOfTeachers.append(list_Of_No_Of_Periods[listOfSubject.index(i)])
            
            # Recieving Name Of the Teacher

            for i in listOfSecetion:
                print("")
                nameOfTeacher = input(f"{i} : ").upper()
                nameOfTeachers.append(nameOfTeacher)

            classInfo.append(nameOfTeachers)

        # Creation Of Table " Class Info "


        sql.execute(f"create table class_{standard} (Subject varchar(50) , No_Of_Periods  int(10) );")

        for i in listOfSecetion:
            sql.execute(f"alter table class_{standard} add ({i} varchar(50));")

        String = ("%s," * (noOfSection + 1))

        for i in classInfo:
            command = "insert into class_" + str(standard) + " values (" + String +"%s);"
            value = i
            sql.execute(command,value)

        # Sorting  Teacher's  Name 

        teachers = []
        sql.execute(f"select * from class_{standard}")

        for m in range(noOfSubject):
            data = sql.fetchone()
            max(m)

            for b in range(2,noOfSection+2):
                teachers.append(data[b])

            for e in range(0,30):
                k=[]
                o=len(teachers)
                for i in range(e+1,(o)):
                    if teachers[e] == teachers[i]:
                        k.append(i)
                k.sort(reverse=True)

                for p in k:
                    teachers.pop(p)
        for s in teachers :
            print(s)

        #  Table Verification 

        sql.execute("show tables")
        data = sql.fetchall()
        sortedTables = []

        for i in data:

            if i[0][0 : 7] == "teacher":
                sortedTables.append(i[0])
            
        #          Teacher's ID Creation

        if not sortedTables == []:
            oldTeacher=[]

            for M in sortedTables :

            # Comparing with Other Tables

                sql.execute(f"select * from {M}")
                data =sql.fetchall()
                lastId = data[len(data)-1][0]
                
                removingTeacher = []

                for i in teachers:

                    for j in range(len(data)):

                        if i == data[j][1]:
                            removingTeacher.append(i)
                            oldTeacher.append(data[j])

                for i in removingTeacher:
                    teachers.remove(i)

            #Creating new Id for New Teacher and File

            newIdList = []

            for i in range((len(teachers))):
                Id = lastId + i
                newIdList.append(Id)

                with open(f"D://Big-Ben//Teachers//{Sector}//{str(Id)}_{teachers[i]}.csv","w") as teacherFile:

                    teacherFileWriter = csv.writer(teacherFile)

                    Value = [["Days","Period-1","Period-2","Period-3","Period-4","Period-5","Period-6","Period-7","Period-8",],
                        ["MON","-","-","-","-","-","-","-","-"],
                        ["TUE","ASS","-","-","-","-","-","-","-"],
                        ["WED","-","-","-","-","-","-","-","-"],
                        ["THUR","ASS","-","-","-","-","-","-","-"],
                        ["FRI","-","-","-","-","-","-","-","-"]]

                    for i in Value:
                        teacherFileWriter.writerow(i)

            #Combining teacher name and Id And Add Old Teacher

            teacher_info = []

            for i in oldTeacher :
                teacher_info.append(i) 

            for i in range(len(teachers)):
                temp = []
                temp.append(newIdList[i])
                temp.append(teachers[i])
                teacher_info.append(temp)

            print(teacher_info)

            #Creation Of Tables 

            sql.execute(f"create table teacher_{standard} (ID int(10) , Name char(50))")

            for i in teacher_info:
                Command = "insert into teacher_" + str(standard) + " values(%s,%s)"
                Value = i
                sql.execute(Command,Value)

        else :
            IdList = []
            teacher_info = []

        # Creating  Id For Teacher And File

            for i in range(len(teachers)):
                Id = 1000 + i
                IdList.append(Id)

                with open(f"D://Big-Ben//Teachers//{Sector}//{str(Id)}_{teachers[i]}.csv","w") as teacherFile:

                    teacherFileWriter = csv.writer(teacherFile)

                    Value = [["Days","Period-1","Period-2","Period-3","Period-4","Period-5","Period-6","Period-7","Period-8",],
                        ["MON","-","-","-","-","-","-","-","-"],
                        ["TUE","ASS","-","-","-","-","-","-","-"],
                        ["WED","-","-","-","-","-","-","-","-"],
                        ["THUR","ASS","-","-","-","-","-","-","-"],
                        ["FRI","-","-","-","-","-","-","-","-"]]

                    for i in Value:
                        teacherFileWriter.writerow(i)
                    
                
        # Combining Name And Id

            for i in range(len(teachers)):
                temp = []
                temp.append(IdList[i])
                temp.append(teachers[i])
                teacher_info.append(temp)

            print(teacher_info)

        #   Creation Of Tables

            sql.execute(f"create table teacher_{standard} (ID int(10) , Name char(50))")

            for i in teacher_info:
                Command = f"insert into teacher_" + str(standard) + " values(%s,%s)"
                Value = i
                sql.execute(Command,Value)

    # Allocation Of Periods 

        Sheduler(standard,conn,Reshedule,Sector)


