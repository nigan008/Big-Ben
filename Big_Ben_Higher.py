#  Importing random Package

import random

#  Importing PYMYSQL And Establishing Connecction With MYSQL

import pymysql
conn=pymysql.connect(host="localhost",user="root",password="",port = 3308)
sql=conn.cursor()

# Importing ErrorHandler(Function) From ErrorHandler(.py File)

from ErrorHandler import ErrorHandler

#  Importing Colorama Package
 
from colorama import init
init()

# Importing CSV Package And OS Module

import csv

import os

# This Function used to shedule Periods For Class 11 And 12 

def Higher_Sheduler(Reshedule,Sector,standard):
    
    sql.execute("use big_ben")
    sql.execute("show tables")
    data = sql.fetchall()
    noOfSection = 0

    for b in data:

        if b[0][0: 8] == f"class_{standard}":
            noOfSection+=1
    
    sql.execute(f"select * from teacher_{standard}")
    TeacherInfo = sql.fetchall()

    for  Name in TeacherInfo :
        teacher = []
        line = 0

        # Change The Teacher's File as Empty Periods  For Reshedule
        
        with open(f"D://Big-Ben//Teachers//{Sector}//{str(Name[0])}_{Name[1]}.csv","r") as teacherFile:
            teacherFileReader = csv.reader(teacherFile)
            
            for g in teacherFileReader:
                if line%2 == 0:
                    teacher.append(g)
                line+=1
            teacherFile.close()

        if Reshedule :
            for c in teacher:
                for j in c:
                    if  j[0:2] == str(standard):
                        teacher[teacher.index(c)][teacher[teacher.index(c)].index(j)] = "-"
        
        with open(f"D://Big-Ben//Teachers//{Sector}//{str(Name[0])}_{Name[1]}.csv","w") as teacherFile:
            teacherFileWriter = csv.writer(teacherFile)
            
            for I in teacher:
                    teacherFileWriter.writerow(I)
            teacherFile.close()

    sql.execute(f"select * from class_{standard}_{chr(65)}")  
    ClassInfo = sql.fetchall()

    noOfSubject = len(ClassInfo)
    totalCount = []
    
    for n in range(noOfSection):
        VAL = []
        len(str(n))

        for m in range(noOfSubject):
            VAL.append(0)
            len(str(m))

        totalCount.append(VAL)

    for repeat in range(2):
        
        for i in range(noOfSection):
            PracDay = [1,2,3,4,5]
            sql.execute(f"select * from class_{standard}_{chr( i + 65)}")
            
            ClassInfo = sql.fetchall()
            
            if repeat == 0:
                classPeriod = [["Days","Period-1","Period-2","Period-3","Period-4","Period-5","Period-6","Period-7","Period-8",],
                                ["MON","-","-","-","-","-","-","-","-"],
                                ["TUE","-","-","-","-","-","-","-","-"],
                                ["WED","-","-","-","-","-","-","-","-"],
                                ["THUR","-","-","-","-","-","-","-","-"],
                                ["FRI","-","-","-","-","-","-","-","-"]]
            
            if repeat == 1:

                classPeriod = []
                line = 0
                
                with open(f"D://Big-Ben//Class//{Sector}//{standard}//{standard}_{chr(i + 65)}.csv","r") as studentFile:
                    studentFileReader = csv.reader(studentFile)
                    for g in studentFileReader:
                        if line%2 == 0:
                            classPeriod.append(g)
                        line+=1
                    studentFile.close()
                
            sql.execute(f"select * from teacher_{standard}")
            TeacherInfo = sql.fetchall()

            for Info in ClassInfo:
                
                for  Name in TeacherInfo :

                    if Info[1] == Name[1]:

                        teacher = []
                        line = 0
                        with open(f"D://Big-Ben//Teachers//{Sector}//{str(Name[0])}_{Name[1]}.csv","r") as teacherFile:
                            teacherFileReader = csv.reader(teacherFile)
                            for g in teacherFileReader:
                                if line%2 == 0:
                                    teacher.append(g)
                                line+=1
                            teacherFile.close() 

                        Day = [1,2,3,4,5]

                        # Obtaining Random Day

                        for l in range(len(Day)):

                            if Info[0][-4:] == "PRAC":
                                day = random.choice(PracDay)                        
                                Period = [3,5,7]

                            else:
                                day = random.choice(Day)
                                Day.remove(day)
                                Period = [1,2,3,4,5,6,7,8]
                                len(str(l))

                            if totalCount[i][ClassInfo.index(Info)] >= Info[2] :
                                break

                            # Obtaining Random Period

                            for k in range(len(Period)):
                                period = random.choice(Period)
                                Period.remove(period)
                                len(str(k))

                            
                                # Condition For Checking Both Students And Teacher Are Free At That Period
                                if Info[0][-4:] == "PRAC":
                                    
                                    if classPeriod[day][period + 1] == "-" and teacher[day][period + 1] == "-" :
                                        if classPeriod[day][period] == "-" and teacher[day][period] == "-":
                                            classPeriod[day][period + 1] = Info[0][0:6].upper() + Info[0][6].lower()
                                            teacher[day][period + 1] = str(standard) + chr(i + 65)  
                                            classPeriod[day][period] = Info[0][0:6].upper() + Info[0][6].lower()
                                            teacher[day][period] = str(standard) + chr(i + 65)                                         
                                            totalCount[i][ClassInfo.index(Info)] += 2 
                                            PracDay.remove(day)
                                            break
                                else:
                                    if classPeriod[day][period] == "-" and teacher[day][period] == "-" :
                                        classPeriod[day][period] = Info[0][0:3].upper()
                                        teacher[day][period] = str(standard) + chr(i + 65)
                                        totalCount[i][ClassInfo.index(Info)] += 1 
                                        break

                            if repeat == 0:
                                if totalCount[i][ClassInfo.index(Info)] >= 5 :
                                    break

                            if repeat == 1:
                                if totalCount[i][ClassInfo.index(Info)] >= Info[2] :
                                    break

                        with open(f"D://Big-Ben//Teachers//{Sector}//{str(Name[0])}_{Name[1]}.csv","w") as teacherFile:
                            teacherFileWriter = csv.writer(teacherFile)
                            for I in teacher:
                                    teacherFileWriter.writerow(I)

            if os.path.exists(f"D://Big-Ben//Class//{Sector}//{standard}"):
                pass

            else:
                os.mkdir(f"D://Big-Ben//Class//{Sector}//{standard}")
                
            with open(f"D://Big-Ben//Class//{Sector}//{standard}//{standard}_{chr(i + 65)}.csv","w") as studentFile:
                studentFileWriter = csv.writer(studentFile)
                for J in classPeriod:
                    studentFileWriter.writerow(J)

    # Datas That Needed To Find Errors In Sheduling 

    PeriodCount = []
    for k in range(len(totalCount[0])):
        VAL = []
        
        for j in range(len(totalCount)):
            VAL.append(0)
        PeriodCount.append(VAL)
    
    for k in range(len(totalCount)):
        for j in range(len(totalCount[k])):
            PeriodCount[j][k] = totalCount[k][j]

    Information = []

    sql.execute(f"select * from class_{standard}_{chr(65)}")
    ClassInfo = sql.fetchall()

    for Subject in range(len(ClassInfo)):
        
        for count in range(noOfSection):
            sql.execute(f"select * from class_{standard}_{chr( count + 65)}")
            ClassInfo = sql.fetchall()
            
            try:
                if not ClassInfo[Subject][2] == PeriodCount[Subject][count] :
                    subInformation = []
                    subInformation.append(ClassInfo[Subject][0])
                    subInformation.append(ClassInfo[Subject][2])
                    subInformation.append(count)
                    Information.append(subInformation)
            except:
                pass
    
    # Key is a variable that used to decide class is (11 to 12 ) or (1 to 10)

    key = 1

    # ErrorHandler is used to find some unallocated period and to Shedule it properly

    ErrorHandler(PeriodCount,ClassInfo,standard,Sector,Information,noOfSection,key)


# -------------------------------------------------------------------------------------------


# This Function Is Used To Store The Teacher's Data Into Mysql For Class 11 And 12

def Higher(Find,standard,Sector,Reshedule):
    
    sql.execute("use big_ben")
    
    if Find:
        print("")
        noOfSection = int(input("No . Of. Section : "))

        # Assining Name Of Section

        listOfSecetion = []
        
        for i in range(noOfSection):
            alphabet = "Section_" + chr( i + 65)
            listOfSecetion.append(alphabet)

        listOfgroup = []
        print("Please Enter The group For The Following Class")
        
        for i in listOfSecetion :
            group = input(f"{i} : ").lower()
            listOfgroup.append(group)
        
        for i in range(len(listOfSecetion)):
            
            if listOfgroup[i] == "biology":
                subject = [["PHY_PRAC"],["CHE_PRAC"],["BIO_PRAC"],["ENGLISH"],["PET"],["BIOLOGY"],["PHYSICS"],["CHEMISTRY"],["MATHS"],["SUPW"]]
            
            if listOfgroup[i] == "computer":
                subject = [["PHY_PRAC"],["CHE_PRAC"],["COM_PRAC"],["ENGLISH"],["PET"],["COMPUTER"],["PHYSICS"],["CHEMISTRY"],["MATHS"],["SUPW"]] 
            
            if listOfgroup[i] == "commerce":
                subject =[["COM_PRAC"],["ENGLISH"],["PET"],["ACCOUNTANCY"],["ECONOMICS"],["BUSSINESS_MATHS"],["MATHS"],["MORAL"]]
            
            print("\033[2J")
            print(f"Enter The  Teacher's Name of {listOfSecetion[i]} for following Subject ")

            teachers = []
            
            for j in range(len(subject)) :
                teacher = input(f"{subject[j][0]} : ").upper()
                subject[j].append(teacher)
                teachers.append(teacher)
            print("\033[2J")
            print(f"Enter The  No of periods for following Subject ")
            
            for q in range(len(subject)) :
                noOfPerioD = int(input(f"{subject[q][0]} : "))
                subject[q].append(noOfPerioD)

            
            sql.execute(f"create table class_{standard}_{listOfSecetion[i][-1].upper()} (Subject varchar(50) , Teacher varchar(50) , No_Of_Periods int(10));")
            
            for k in subject:
                command = "insert into class_" + str(standard) + "_" + str(listOfSecetion[i][-1].upper()) + " values (%s,%s,%s);"
                value = k
                sql.execute(command,value)
            
            sql.execute("show tables")
            data = sql.fetchall()
            sortedTables = []
            
            for l in data:
                
                if l[0][0 : 7] == "teacher":
                    sortedTables.append(l[0])
                
            #          Teacher's ID Creation
            lastIdSelection = []
            
            if not sortedTables == []:
                oldTeacher=[]
                
                for M in sortedTables :

                # Comparing with Other Tables
                    
                    sql.execute(f"select * from {M}")
                    data =sql.fetchall()
                    
                    for A in data:
                        lastIdSelection.append(A[0])
                    
                    
                    removingTeacher = []
                    
                    for z in teachers:
                        
                        for j in range(len(data)):
                            
                            if z == data[j][1]:
                                removingTeacher.append(z)
                                oldTeacher.append(data[j])
                    for z in removingTeacher:
                        
                        try:
                            teachers.remove(z)
                        except:
                            pass

                    lastId = max(lastIdSelection)

                #Creating new Id for New Teacher and File

                newIdList = []
                
                for z in range((len(teachers))):
                    Id = lastId + z + 1 
                    newIdList.append(Id)
                    
                    with open(f"D://Big-Ben//Teachers//{Sector}//{str(Id)}_{teachers[z]}.csv","w") as teacherFile:
                        teacherFileWriter = csv.writer(teacherFile)
                        Value = [["Days","Period-1","Period-2","Period-3","Period-4","Period-5","Period-6","Period-7","Period-8",],
                            ["MON","-","-","-","-","-","-","-","-"],
                            ["TUE","-","-","-","-","-","-","-","-"],
                            ["WED","-","-","-","-","-","-","-","-"],
                            ["THUR","-","-","-","-","-","-","-","-"],
                            ["FRI","-","-","-","-","-","-","-","-"]]
                        
                        for y in Value:
                            teacherFileWriter.writerow(y)

                #Combining teacher name and Id And Add Old Teacher
                
                teacher_info = [] 

                for p in oldTeacher :
                    teacher_info.append(p)

                for y in range(len(teachers)):
                    temp = []
                    temp.append(newIdList[y])
                    temp.append(teachers[y])
                    teacher_info.append(temp)

                #Creation Of Tables 
                sql.execute("show tables")
                data = sql.fetchall()
                sortedTables = []
                
                for l in data:
                    
                    if l[0] == f"teacher_{standard}":
                        break
                else:
                    sql.execute(f"create table teacher_{standard} (ID int(10) , Name char(50) )")

                for z in teacher_info:
                    Command = "insert into teacher_" + str(standard) + " values(%s,%s)"
                    Value = z
                    sql.execute(Command,Value)
            else :

                IdList = []
                teacher_info = []
            
            # Creating  Id For Teacher And File
                
                for z in range(len(teachers)):
                    Id = 1000 + z
                    IdList.append(Id)
                    
                    with open(f"D://Big-Ben//Teachers//{Sector}//{str(Id)}_{teachers[z]}.csv","w") as teacherFile:
                        teacherFileWriter = csv.writer(teacherFile)
                        Value = [["Days","Period-1","Period-2","Period-3","Period-4","Period-5","Period-6","Period-7","Period-8",],
                            ["MON","-","-","-","-","-","-","-","-"],
                            ["TUE","-","-","-","-","-","-","-","-"],
                            ["WED","-","-","-","-","-","-","-","-"],
                            ["THUR","-","-","-","-","-","-","-","-"],
                            ["FRI","-","-","-","-","-","-","-","-"]]
                        
                        for y in Value:
                            teacherFileWriter.writerow(y)
                        
                    
            # Combining Name And Id
                
                for z in range(len(teachers)):
                    temp = []
                    temp.append(IdList[z])
                    temp.append(teachers[z])
                    teacher_info.append(temp)

            #   Creation Of Tables

                sql.execute(f"create table teacher_{standard} (ID int(10) , Name char(50) )")
                
                for z in teacher_info:
                    Command = f"insert into teacher_" + str(standard) + " values(%s,%s)"
                    Value = z
                    sql.execute(Command,Value)

        Higher_Sheduler(Reshedule,Sector,standard)


        
                
            
