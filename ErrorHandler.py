#  Importing PYMYSQL And Establishing Connecction With MYSQL

import pymysql
conn=pymysql.connect(host="localhost",user="root",password="",port = 3308)
sql=conn.cursor()

# Importing csv Package

import csv

# ErrorHandler Is Used To Find Some Unallocated Period And To Shedule It Properly

def ErrorHandler(PeriodCount,ClassInfo,standard,Sector,Information,noOfSection,key):
    

    for SECTION in range(len(Information)):
        classes = Information[SECTION][2]
        Classes =[]
        line = 0

        with open(f"D://Big-Ben//Class//{Sector}//{standard}//{standard}_{chr(classes + 65)}.csv","r") as classFile:
            classFileReader = csv.reader(classFile)

            for g in classFileReader:
                if line%2 == 0:
                    Classes.append(g)
                line+=1

            classFile.close()

        dayPeriod = []
        
        for day in range(1,6):
           
            for period in range(1,9):
                
                if Classes[day][period] == "-" :
                    subdayPeriod = []
                    subdayPeriod.append(day)
                    subdayPeriod.append(period)
                    dayPeriod.append(subdayPeriod)

        subjectInfo = []
        
        for Number in dayPeriod :
            
            Classes =[]
            line = 0
            
            with open(f"D://Big-Ben//Class//{Sector}//{standard}//{standard}_{chr(classes + 65)}.csv","r") as classFile:
                classFileReader = csv.reader(classFile)

                for g in classFileReader:
                    if line%2 == 0:
                        Classes.append(g)
                    line+=1

                classFile.close()

            if key == 1:
                sql.execute("use big_ben")
                sql.execute(f"select * from class_{standard}_{chr( classes + 65)}")
                ClassInfo = sql.fetchall()

            for Name in ClassInfo:
                if not Name[0][0:3] == Information[SECTION][0][0:3] and not Name[0][-4:] == "PRAC":
                    subjectInfo.append(Name[0][0:3])
            
            for i in subjectInfo:
                if i == "-":
                    subjectInfo.remove(i)

            for i in subjectInfo:
                count = 0
                for j in subjectInfo:
                    if i == j :
                        count += 1
                        if count == 2:
                            subjectInfo.remove(i)
                            subjectInfo.remove(i)

            SubjectName = []

            for subject in subjectInfo:
                
                for Name in ClassInfo :
                    
                    if subject == Name[0][0:3] :
                        
                        if key == 0:
                            
                            if Name[1] < 5 or Name[1] > 5 :
                                Value = []
                                Value.append(Name[0])
                                Value.append(Name[1])
                                SubjectName.append(Value)
                        if key == 1:
                           
                            if (Name[2] < 5 or Name[2] > 5) and not Name[0][-4:] == "PRAC" :
                                Value = []
                                Value.append(Name[0])
                                Value.append(Name[2])
                                SubjectName.append(Value)

            removing = []
            
            for subject in SubjectName:
                SubjectCount = 0
                
                for period in range(1,9):
                    if Classes[Number[0]][period] == subject[0][0:3] :
                        SubjectCount +=1
                
                if subject[1] < 5:
                    if SubjectCount > 0 :
                        removing.append(subject)
                        
                if subject[1] > 5:
                    if SubjectCount > 1 :
                        removing.append(subject)
            
            for i in removing:
                SubjectName.remove(i)
            
            SelectedDay = []

            for subject in SubjectName:
                
                for day in range(1,6):
                    SubjectCount = 0
                    
                    if not day == Number[0]:

                        for period in range(1,9):
                            if key == 0 :
                                if Classes[day][period] == subject[0][0:3]  :
                                    SubjectCount +=1

                            if key == 1 :
                                if Classes[day][period] == subject[0][0:3] and not Classes[day][period][-3:] == "PRa" :
                                    SubjectCount +=1

                        if subject[1] < 5:
                            
                            if SubjectCount == 1 :
                                value = []
                                value.append(subject[0])
                                value.append(day)
                                SelectedDay.append(value)
                            
                        if subject[1] > 5 :
                            
                            if SubjectCount == 2 :
                                value = []
                                value.append(subject[0])
                                value.append(day)
                                SelectedDay.append(value)

                        SubjectCount = 0
                        
                        for period in range(1,9):
                            
                            if key == 0 :
                                if Information[SECTION][0][0:3] == Classes[day][period]  :
                                    SubjectCount +=1
                            
                            if key == 1 :
                                if Information[SECTION][0][0:3] == Classes[day][period] and not Classes[day][period][-3:] == "PRa":
                                    SubjectCount+=1
                            
                        if Information[SECTION][1] < 5:
                            if SubjectCount == 0 :
                                pass
                            
                            else :
                                
                                for i in SelectedDay :
                                    if i[1] == day :
                                        SelectedDay.remove(i)

                            
                        if Information[SECTION][1] > 5 :
                            if SubjectCount == 1 :
                                pass

                            else:
                                for i in SelectedDay :
                                    if i[1] == day :
                                        SelectedDay.remove(i)

            for day in SelectedDay :
                val= []
                for period in range(1,9):
                    if Classes[day[1]][period] == day[0][0:3]:
                        val.append(period)
                day.append(val)
            
            for data in SelectedDay:
                for i in ClassInfo:
                    if data[0] == i[0] :
                        if key == 0 :
                            data.append(i[2+classes])
                        if key == 1:
                            data.append(i[1])
                
                sql.execute("use big_ben;")
                sql.execute("show tables")
                info = sql.fetchall()

                # Checking For Teacher's Name
                
                for i in info:
                    a = i[0][0:7]

                    if a == "teacher":
                        sql.execute(f"select * from {i[0]}")
                        teacherData = sql.fetchall()

                        for j in teacherData:

                            if j[1] == data[3]:
                                data.append(j[0])
                                break


            changeTeacher = []
            for i in ClassInfo:
                if Information[SECTION][0] == i[0] :
                    changeTeacher.append(Information[SECTION][0])
                    
                    if key == 0 :
                        changeTeacher.append(i[2+classes])
                    if key == 1 :
                        changeTeacher.append(i[1])

            sql.execute("use big_ben;")
            sql.execute("show tables")
            info = sql.fetchall()

            for i in info:
                a = i[0][0:7]

                if a == "teacher":
                    sql.execute(f"select * from {i[0]}")
                    teacherData = sql.fetchall()

                    for j in teacherData:

                        if j[1] == changeTeacher[1]:
                            changeTeacher.append(j[0])
                            break
    
            for data in SelectedDay:
                line = 0
                subteacher = []
                
                with open(f"D://Big-Ben//Teachers//{Sector}//{str(data[4])}_{data[3]}.csv","r") as subteacherFile:
                    subteacherFileReader = csv.reader(subteacherFile)

                    for g in subteacherFileReader:
                        if line%2 == 0:
                            subteacher.append(g)
                        line+=1

                    subteacherFile.close()

                line = 0
                chngteacher = []
                
                with open(f"D://Big-Ben//Teachers//{Sector}//{changeTeacher[2]}_{changeTeacher[1]}.csv","r") as chngteacherFile:
                    chngteacherFileReader = csv.reader(chngteacherFile)
                    
                    for g in chngteacherFileReader:
                        if line%2 == 0:
                            chngteacher.append(g)
                        line+=1

                    chngteacherFile.close()
                Find = False
                
                for j in data[2]:
                    if subteacher[Number[0]][Number[1]] == "-" and chngteacher[data[1]][j] == "-" :
                        subteacher[Number[0]][Number[1]] = str(standard)+ chr(classes + 65)
                        chngteacher[data[1]][j] = str(standard)+ chr(classes + 65)
                        Classes[Number[0]][Number[1]] = data[0]
                        Classes[data[1]][j] = changeTeacher[0]
                        Find = True
                        break
                
                if Find :
                    break
            

            with open(f"D://Big-Ben//Class//{Sector}//{standard}//{standard}_{chr(classes + 65)}.csv","w") as studentFile:
                studentFileWriter = csv.writer(studentFile)
                for ClassPeriod in Classes:
                    studentFileWriter.writerow(ClassPeriod)

            studentFile.close()

            with open(f"D://Big-Ben//Teachers//{Sector}//{changeTeacher[2]}_{changeTeacher[1]}.csv","w") as chngteacherFile:
                chngteacherFileWriter = csv.writer(chngteacherFile)
                for I in chngteacher:
                    chngteacherFileWriter.writerow(I)
                chngteacherFile.close()
            
            with open(f"D://Big-Ben//Teachers//{Sector}//{str(data[4])}_{data[3]}.csv","w") as subteacherFile:
                subteacherFileWriter = csv.writer(subteacherFile)
                for I in subteacher:
                    subteacherFileWriter.writerow(I)
                subteacherFile.close()                

    print(f" The Time Table Of Teachers Is Created In The D: / Big-Ben / Teachers /{Sector} : ")
    print("")
    print(f" The Time Table Of Students Is Created In The D: / Big-Ben / Class / {Sector} / {standard} : ")
    print("")
    print("")
    print("               ! ! Time Table Is Successfully Sheduled  ! !")
    print("")
    print("")
