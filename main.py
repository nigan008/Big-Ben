import pymysql

conn=pymysql.connect(host="localhost",user="root",password="",db="project")
a=conn.cursor()

""" sql ="insert into std_12 values(%s,%s,%s,%s,%s,%s,%s);"
val=['SUPW','1','NTR','NTR','NTR','NTR','NTR']
a.execute(sql,val) """

"""data =a.fetchone()
for i in data:
    print(i) """

teachers = []
noOfSection = 5
a.execute("select * from std_12")


    
#         Sorting  Teacher's  Name 

for m in range(5):
    data = a.fetchone()
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

 
#          Teacher's ID Creation

def checking(teacher):
    try:

    # Comparinprig with Other Tables

        a.execute("select * from teacher")
        data =a.fetchall()
        lastId = data[len(data)-1][0]
        oldTeacher=[]
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

    #  Combining teacher name and Id And Add Old Teacher

        teacher_info = []
        for i in oldTeacher :
            teacher_info.append(i) 
        for i in range(len(teacher)):
            temp = []
            temp.append(newIdList[i])
            temp.append(teacher[i])
            teacher_info.append(temp)
        print(teacher_info)

    #   Creation Of Tables 

        a.execute("create table 11teacher (ID int(10) , Name char(50))")
        for i in teacher_info:
            Command = "insert into 11teacher values(%s,%s)"
            Value = i
            a.execute(Command,Value)
            
   

    except :
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

        a.execute("create table 12teacher (ID int(10) , Name char(50))")
        for i in teacher_info:
            Command = "insert into 12teacher values(%s,%s)"
            Value = i
            a.execute(Command,Value)
        
checking(teachers)



