import pymysql
conn=pymysql.connect(host="localhost",user="root",password="",db="project")
sql=conn.cursor()



from colorama import init
init()

# Recieving Input From Admin

standard = int(input("STANDARAD : "))
print("")
noOfSubject = int(input("No . Of . Subject :"))
print("")
noOfSection = int(input("No . Of. Section :"))

# Assining Name Of Section

listOfSecetion = []
for i in range(noOfSection):
    alphabet = "Section_" + chr( i + 65)
    listOfSecetion.append(alphabet)

# Recieving Name Of The Subject From Admin

listOfSubject = []

print("\033[2J")
print("Please Enter The Name Of Subjects")
for i in range(noOfSubject):
    print('')
    subject = input(f"Name Of Subject {i + 1} :")
    listOfSubject.append(subject)

# Recieving No Of Periods per Week for Each Subject From Admin

list_Of_No_Of_Periods = []

print("\033[2J")
print("Please Enter The No of Periods Per Week According To Thier Subject")

for i in listOfSubject:
    noOfPeriod = int(input(f"{i}"))
    list_Of_No_Of_Periods.append(noOfPeriod) 

#  Recieving Class Info

classInfo = []

for i in listOfSubject :
    print("\033[2J")
    print (f"Please Enter The  Name Of  {i} Teacher According To Thier Section ")

    # Appending Name Of Subject And NoOf Periods 
    nameOfTeachers = []
    nameOfTeachers.append(i)
    nameOfTeachers.append(list_Of_No_Of_Periods[listOfSubject.index(i)])
    

    # Recieving Name Of the Teacher

    for i in listOfSecetion:
        nameOfTeacher = input(f"{i} :")
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

#         Sorting  Teacher's  Name 

teachers = []
sql.execute(f"select * from class_{standard}")

for m in range(5):
    data = sql.fetchone()
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

def checking(teacher):

    if not sortedTables == []:
        oldTeacher=[]
        for M in sortedTables :

        # Comparing with Other Tables

            sql.execute(f"select * from {M}")
            data =sql.fetchall()
            lastId = data[len(data)-1][0]
            
            removingTeacher = []
            for i in teacher:
                for j in range(len(data)):
                    if i == data[j][1]:
                        removingTeacher.append(i)
                        oldTeacher.append(data[j])
            for i in removingTeacher:
                teacher.remove(i)

        #Creating new Id for New Teacher

        newIdList = []
        for i in range(1,(len(teacher)+1)):
            Id = lastId + i
            newIdList.append(Id)

        #Combining teacher name and Id And Add Old Teacher

        teacher_info = []
        for i in oldTeacher :
            teacher_info.append(i) 
        for i in range(len(teacher)):
            temp = []
            temp.append(newIdList[i])
            temp.append(teacher[i])
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
    # Creating  Id For Teacher
        for i in range(len(teacher)):
            Id = 1000 + i
            IdList.append(Id)
    # Combining Name And Id
        for i in range(len(teacher)):
            temp = []
            temp.append(IdList[i])
            temp.append(teacher[i])
            teacher_info.append(temp)
        print(teacher_info)

    #   Creation Of Tables

        sql.execute(f"create table teacher_{standard} (ID int(10) , Name char(50))")
        for i in teacher_info:
            Command = f"insert into teacher_" + str(standard) + " values(%s,%s)"
            Value = i
            sql.execute(Command,Value)
        
checking(teachers)



