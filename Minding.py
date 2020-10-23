#Importing CSV Module

import csv

#  Importing random Package

import random

# Importing OS Module

import os

# Importing datetime from date module

from datetime import date

def Minding():
    print("")
    print("")
    print("                       Big Ben")
    print("")
    print("")
    today = date.today()

    if os.path.exists("D://Big-Ben//Mindings"):
        pass

    else:
        os.mkdir("D://Big-Ben//Mindings")


    # Recieving Input From Admin
    
    Sector = input("SECTOR : ")
    print("")

    if os.path.exists(f"D://Big-Ben//Mindings//{Sector}"):
        pass

    else:
        os.mkdir(f"D://Big-Ben//Mindings//{Sector}")

    absentDay = input("Day : ")
    print("")

    noOfTeachers = int(input("No . Of . Teachers Absent : "))
    print("")

    teachersList = []

    for i in range(noOfTeachers):
        List = []
        teacherId = input("Teacher's ID : ").upper()
        print("")
        teacherName = input("Teacher's  Name : ").upper()
        print("")
        List.append(teacherId)
        List.append(teacherName)
        teachersList.append(List)

    # Opening Absentes Teacher File 

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

    # Converting Days As Numbers To Access The List

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

    # Getting Information Of The Absented Teacher's Periods

        for period in range(1,9):

            if teacher[day][period] != "-" and teacher[day][period] != "ASS":

                data = []
                data.append(period)
                data.append(teacher[day][period])
                holder.append(data)

        print(holder)

        # Recieving All The Teacher's File In The Sector(Folder) To Obtain Free Periods Of Teacher 

        allTeachers = os.listdir(f"D://Big-Ben//Teachers//{Sector}")
        
        # Removing The Absented Teacher From The List Of Teachers  In Sector

        for j in range(noOfTeachers):

            for Check in allTeachers:

                if teachersList[j][1] == Check[5:-4] :
                    allTeachers.remove(Check)

        allocatedTeacher = []

        # Checking The Free  Periods Of Teacher

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

                # IF The Teacher is Free At The Period Will be Selected

                if teacher[day][data[0]] == "-":

                    mindingData.append(Teacher[5:-4])
                    mindingData.append(data[0])
                    mindingData.append(data[1])
                    selectedTeachers.append(mindingData)  

            # Using Random Obtain The Teacher For Minding Periods

            randomTeachers = random.choice(selectedTeachers)
            allocatedTeacher.append(randomTeachers)

        # Writing Information Into The File (CSV)

        with open(f"D://Big-Ben//Mindings//{Sector}//{today}.csv","w") as teacherFile:

                teacherFileWriter = csv.writer(teacherFile)
                teacherFileWriter.writerow(["Minding Teacher","Period","Class"])

                for I in allocatedTeacher:
                        teacherFileWriter.writerow(I)

    
