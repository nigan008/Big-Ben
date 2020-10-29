#  Importing random Package

import random

# Importing CSV Package And OS Module

import csv

#  Importing OS Module

import os

# Importing ErrorHandler(Function) From ErrorHandler(.py File)

from ErrorHandler import ErrorHandler

# A Function To Shedule The Periods For Teachers And Students

def Sheduler(standard,conn,Reshedule,Sector):

    # Importing PYMYSQL And Establishing Connecction With MYSQL

    import pymysql
    sql=conn.cursor()

    #  Recieving ClassInfo from Database

    sql.execute(f"select * from class_{standard}")
    ClassInfo = sql.fetchall()
    noOfSection = len(ClassInfo[0]) - 2

    # Creating pre Shedule for Whole Class

    wholeClassPeriod = []
    for i in range(noOfSection) :

        classPeriod = [["Days","Period-1","Period-2","Period-3","Period-4","Period-5","Period-6","Period-7","Period-8",],
                        ["MON","-","-","-","-","-","-","-","-"],
                        ["TUE","-","-","-","-","-","-","-","-"],
                        ["WED","-","-","-","-","-","-","-","-"],
                        ["THUR","-","-","-","-","-","-","-","-"],
                        ["FRI","-","-","-","-","-","-","-","-"]]   
                        
        wholeClassPeriod.append(classPeriod)

    # Recieving TeacherInfo from Database

    sql.execute(f"select * from teacher_{standard}")
    TeacherInfo = sql.fetchall()

    # Change The Teacher's File as Empty Periods  For Reshedule

    for Name in range(len(TeacherInfo)):
        teacher = []
        line = 0

        with open(f"D://Big-Ben//Teachers//{Sector}//{str(TeacherInfo[Name][0])}_{TeacherInfo[Name][1]}.csv","r") as teacherFile:
            teacherFileReader = csv.reader(teacherFile)

            for g in teacherFileReader:
                if line%2 == 0:
                    teacher.append(g)
                line+=1

            teacherFile.close() 

        if Reshedule :
            for i in teacher:
                for j in i:
                    P = j[0:-1]
                    if  P == str(standard):
                        teacher[teacher.index(i)][teacher[teacher.index(i)].index(j)] = "-"

        with open(f"D://Big-Ben//Teachers//{Sector}//{str(TeacherInfo[Name][0])}_{TeacherInfo[Name][1]}.csv","w") as teacherFile:
            teacherFileWriter = csv.writer(teacherFile)
            for I in teacher:
                teacherFileWriter.writerow(I)
            teacherFile.close()

    Section =[]

    # totalcount is to keep the datas of no of periods is sheduled to the respective subjects

    noOfSubject = len(ClassInfo)
    totalCount = []

    for n in range(noOfSubject):
        VAL = []
        len(str(n))

        for m in range(noOfSection):
            VAL.append(0)
            len(str(m))

        totalCount.append(VAL)

    for repeat in range(2):

        for Name in range(len(TeacherInfo)) :
            
            # Recieving File Of Teacher As Per The ID
        
            teacher = []
            line = 0

            with open(f"D://Big-Ben//Teachers//{Sector}//{str(TeacherInfo[Name][0])}_{TeacherInfo[Name][1]}.csv","r") as teacherFile:
                teacherFileReader = csv.reader(teacherFile)

                for g in teacherFileReader:
                    if line%2 == 0:
                        teacher.append(g)
                    line+=1

                teacherFile.close() 
        
            # Obtaining Section , No_Of_Periods , Subject of the Respective Teacher

            for sub in range(len(ClassInfo)):
                
                for i in range(len(ClassInfo[sub])):
                    if ClassInfo[sub][i] == TeacherInfo[Name][1] :
                        Section.append(i-2)
                
                # Obtaining Random Section
                
                for i in range(len(Section)) :
                    section = random.choice(Section)
                    Section.remove(section)
                    
                    Day = [1,2,3,4,5]

                    # Obtaining Random Day

                    for l in range(len(Day)):
                        day = random.choice(Day)
                        Day.remove(day)
                        Period = [1,2,3,4,5,6,7,8]
                        len(str(l))

                        if totalCount[sub][section] == ClassInfo[sub][1]:
                            break
                        
                        # Obtaining Random Period

                        for k in range(len(Period)):
                            period = random.choice(Period)
                            Period.remove(period)
                            len(str(k))

                            # Condition For Checking Both Students And Teacher Are Free At That Period

                            if wholeClassPeriod[section][day][period] == "-" and teacher[day][period] == "-" :
                                wholeClassPeriod[section][day][period] = ClassInfo[sub][0][0:3].upper()
                                teacher[day][period] = str(standard) + chr(section + 65)
                                totalCount[sub][section] += 1 
                                break

                        if repeat == 0:

                            if  totalCount[sub][section] == 5 :  
                                break
                        
                            if  totalCount[sub][section] == ClassInfo[sub][1] :  
                                break
              
            # Storing Data into Teacher's File

            with open(f"D://Big-Ben//Teachers//{Sector}//{str(TeacherInfo[Name][0])}_{TeacherInfo[Name][1]}.csv","w") as teacherFile:
                teacherFileWriter = csv.writer(teacherFile)
                for I in teacher:
                    teacherFileWriter.writerow(I)
                teacherFile.close()
            
        # Storing Data Into Class Files

        if repeat == 1:
            if os.path.exists(f"D://Big-Ben//Class//{Sector}//{standard}"):
                pass

            else:
                os.mkdir(f"D://Big-Ben//Class//{Sector}//{standard}")
                
            for SECTION in wholeClassPeriod:

                with open(f"D://Big-Ben//Class//{Sector}//{standard}//{standard}_{chr(wholeClassPeriod.index(SECTION) + 65)}.csv","w") as studentFile:
                    studentFileWriter = csv.writer(studentFile)
                    for ClassPeriod in SECTION:
                        studentFileWriter.writerow(ClassPeriod)

                    studentFile.close()
    

    # Datas That Needed To Find Errors In Sheduling 

    PeriodCount = totalCount

    Information = []
    for Subject in range(len(ClassInfo)):
        for count in range(len(ClassInfo[Subject])-2):
            if not ClassInfo[Subject][1] == PeriodCount[Subject][count] :
                subInformation = []
                subInformation.append(ClassInfo[Subject][0])
                subInformation.append(ClassInfo[Subject][1])
                subInformation.append(count)
                Information.append(subInformation)

    # Key is a variable that used to decide class is (11 to 12 ) or (1 to 10)

    key = 0

    # ErrorHandler is used to find some unallocated period and to Shedule it properly

    ErrorHandler(PeriodCount,ClassInfo,standard,Sector,Information,noOfSection,key)