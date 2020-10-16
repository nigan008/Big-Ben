import csv
import random
import os
from datetime import date
today = date.today()

if os.path.exists("D://Big-Ben//Mindings"):
    pass
else:
    os.mkdir("D://Big-Ben//Mindings")


Sector = input("SECTOR : ")


if os.path.exists(f"D://Big-Ben//Mindings//{Sector}"):
    pass
else:
    os.mkdir(f"D://Big-Ben//Mindings//{Sector}")

absentDay = input("Day : ")

noOfTeachers = int(input("No . Of . Teachers Absent : "))

teachersList = []

for i in range(noOfTeachers):
    List = []
    teacherId = input("Teacher's ID : ")
    teacherName = input("Teacher's  Name : ")
    List.append(teacherId)
    List.append(teacherName)
    teachersList.append(List)

for i in range(noOfTeachers):
    teacher = []
    line=0
    with open(f"D://Big-Ben//Teachers//{Sector}//{str(teachersList[i][0])}_{teachersList[i][1]}.csv") as teacherFile:
        teacherFileReader = csv.reader(teacherFile)
        for g in teacherFileReader:
            if line%2 == 0:
                teacher.append(g)
            line+=1
        teacherFile.close()

    if absentDay.lower() == "monday":
        day = 1
    if absentDay.lower() == "tuesday":
        day = 2
    if absentDay.lower() == "wednesday":
        day = 3
    if absentDay.lower() == "thursday":
        day = 4
    if absentDay.lower() == "friday":
        day = 5
    
    holder = []

    for period in range(1,9):
        if teacher[day][period] != "-" and teacher[day][period] != "ASS":
            data = []
            data.append(period)
            data.append(teacher[day][period])
            holder.append(data)

    print(holder)

    allTeachers = os.listdir(f"D://Big-Ben//Teachers//{Sector}")

    for j in range(noOfTeachers):
        for Check in allTeachers:
            if teachersList[j][1] == Check[5:-4] :
                allTeachers.remove(Check)

    allocatedTeacher = []

    for data in holder:
        selectedTeachers = []
        for Teacher in allTeachers:
            teacher=[]
            line=0
            with open(f"D://Big-Ben//Teachers//{Sector}//{Teacher}") as teacherFile:
                teacherFileReader = csv.reader(teacherFile)
                for g in teacherFileReader:
                    if line%2 == 0:
                        teacher.append(g)
                    line+=1
                teacherFile.close()

            mindingData = []
            if teacher[day][data[0]] == "-":
                mindingData.append(Teacher[5:-4])
                mindingData.append(data[0])
                mindingData.append(data[1])
                selectedTeachers.append(mindingData)      
        randomTeachers = random.choice(selectedTeachers)
        allocatedTeacher.append(randomTeachers)


    if os.path.exists(f"D://Big-Ben//Mindings//{Sector}//{today}.csv"):
        with open(f"D://Big-Ben//Mindings//{Sector}//{today}.csv","a") as teacherFile:
                teacherFileWriter = csv.writer(teacherFile)
                for I in allocatedTeacher:
                        teacherFileWriter.writerow(I)
    else:
        with open(f"D://Big-Ben//Mindings//{Sector}//{today}.csv","w") as teacherFile:
                teacherFileWriter = csv.writer(teacherFile)
                teacherFileWriter.writerow(["Minding Teacher","Period","Class"])
                for I in allocatedTeacher:
                        teacherFileWriter.writerow(I)

    
