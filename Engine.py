#  Importing random Package

import random

# Importing CSV Package

import csv

# A Function To Shedule The Periods For Teachers And Students

def Sheduler(standard,conn,Reshedule):
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
                        ["TUE","ASS","-","-","-","-","-","-","-"],
                        ["WED","-","-","-","-","-","-","-","-"],
                        ["THUR","ASS","-","-","-","-","-","-","-"],
                        ["FRI","-","-","-","-","-","-","-","-"]]   
        wholeClassPeriod.append(classPeriod)

    # Recieving TeacherInfo from Database

    sql.execute(f"select * from teacher_{standard}")
    TeacherInfo = sql.fetchall()

    Section =[]

    # Obtaining Teacher's Name 

    for Name in range(len(TeacherInfo)) :
        
        # Recieving File Of Teacher As Per The ID
    
        teacher = []
        line = 0
        with open(f"Teachers//{str(TeacherInfo[Name][0])}_{TeacherInfo[Name][1]}.csv","r") as teacherFile:
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

        
        # Obtaining Section , No_Of_Periods , Subject of the Respective Teacher

        for sub in range(len(ClassInfo)):
            
            for i in range(len(ClassInfo[sub])):
                if ClassInfo[sub][i] == TeacherInfo[Name][1] :
                    Section.append(i-2)
            
            # Obtaining Random Section

            for i in range(len(Section)) :
                section = random.choice(Section)
                Section.remove(section)
                count = 0

                # Program For The Subject More Than 5 Periods per Week

                if ClassInfo[sub][1] > 5 :
                    times = 2
                else:
                    times = 1
                for p in range(times):
                    
                    Day = [1,2,3,4,5]
                    len(str(p))

                    # Obtaining Random Day

                    for l in range(len(Day)):
                        day = random.choice(Day)
                        Day.remove(day)
                        Period = [1,2,3,4,5,6,7,8]
                        len(str(l))

                        # Obtaining Random Period

                        for k in range(len(Period)):
                            period = random.choice(Period)
                            Period.remove(period)
                            len(str(k))

                            # Condition For Checking Both Students And Teacher Are Free At That Period

                            if wholeClassPeriod[section][day][period] == "-" and teacher[day][period] == "-" :
                                wholeClassPeriod[section][day][period] = ClassInfo[sub][0][0:3].upper()
                                teacher[day][period] = str(standard) + chr(section + 65)
                                count += 1 
                                break
                        if count == ClassInfo[sub][1] :
                            break
                            
        # Storing Data into Teacher's File

        with open(f"Teachers//{str(TeacherInfo[Name][0])}_{TeacherInfo[Name][1]}.csv","w") as teacherFile:
            teacherFileWriter = csv.writer(teacherFile)
            for I in teacher:
                    teacherFileWriter.writerow(I)
              
    # Storing Data Into Class Files
        
    for Section in wholeClassPeriod:
        with open(f"Class//{standard}_{chr(wholeClassPeriod.index(Section) + 65)}.csv","w") as studentFile:
            studentFileWriter = csv.writer(studentFile)
            for ClassPeriod in Section:
                studentFileWriter.writerow(ClassPeriod)
    


