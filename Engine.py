#  Importing random Package

import random

# Importing PYMYSQL And Establishing Connecction With MYSQL

import pymysql
conn=pymysql.connect(host="localhost",user="root",password="",db="project")
sql=conn.cursor()

# A Function To Shedule The Periods For Teachers And Students

def Sheduler(standard):

    #  Recieving ClassInfo from Database

    sql.execute(f"select * from class_{standard}")
    ClassInfo = sql.fetchall()

    noOfSection = len(ClassInfo[0][0]) - 2

    # Creating pre Shedule for Whole Class

    wholeClassPeriod = []
    for i in range(noOfSection) :
        classPeriod = [[0,0,0,0,0,0,0,0],
                    ["Ass",0,0,0,0,0,0,0],  
                    [0,0,0,0,0,0,0,0],
                    ["Ass",0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0]]     
        wholeClassPeriod.append(classPeriod)

    # Recieving TeacherInfo from Database

    sql.execute(f"select * from teacher_{standard}")
    TeacherInfo = sql.fetchall()

    Section =[]

    Teacher = []

    # Obtaining Teacher's Name 

    for Name in range(len(TeacherInfo)) :
        
        # Recieving File Of Teacher As Per The ID

        teacher = [[0,0,0,0,0,0,0,0],
                ["Ass",0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                ["Ass",0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0]]
        
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
                    for p in range(2):
                        Day = [0,1,2,3,4]
                        len(str(p))

                        # Obtaining Random Day

                        for l in range(len(Day)):
                            day = random.choice(Day)
                            Day.remove(day)
                            Period = [0,1,2,3,4,5,6,7]
                            len(str(l))

                            # Obtaining Random Period

                            for k in range(len(Period)):
                                period = random.choice(Period)
                                Period.remove(period)
                                len(str(k))

                                # Condition For Checking Both Students And Teacher Are Free At That Period

                                if wholeClassPeriod[section][day][period] == 0 and teacher[day][period] == 0 :
                                    wholeClassPeriod[section][day][period] = ClassInfo[sub][0]
                                    teacher[day][period] = str(standard) + chr(section + 65)
                                    count += 1 
                                    break
                            if count == ClassInfo[sub][1] :
                                break
                
                # Program For The Subject Less Than 5 Periods

                else:
                    Day = [0,1,2,3,4]

                    # Obtaining Random Day

                    for l in range(len(Day)):
                        day = random.choice(Day)
                        Day.remove(day)
                        Period = [0,1,2,3,4,5,6,7]

                        # Obtaining Random Period

                        for k in range(len(Period)):
                            period = random.choice(Period)
                            Period.remove(period)
                            
                            # Condition For Checking Both Students And Teacher Are Free At That Period
                            
                            if wholeClassPeriod[section][day][period] == 0 and teacher[day][period] == 0 :
                                wholeClassPeriod[section][day][period] = ClassInfo[sub][0]
                                teacher[day][period] = str(standard) + chr(section + 65)
                                count += 1 
                                break
                        if count == ClassInfo[sub][1] :
                            break

        Teacher.append(teacher)
        
    print(wholeClassPeriod)
    print(Teacher)
    


