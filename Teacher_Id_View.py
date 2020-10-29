#  Importing PYMYSQL And Establishing Connecction With MYSQL

import pymysql
conn=pymysql.connect(host="localhost",user="root",password="",port = 3308)
sql=conn.cursor()

# Used To Find ID Of The Teacher

def Id_View():
    Exist = False

    sql.execute("use big_ben")
    sql.execute("show tables")
    data = sql.fetchall()

    for i in data:
        a = i[0][0:7]
        if a == "teacher":
            Exist = True

    if Exist :

        print("\033[2J")
        print("")
        print("")
        print("                       Big Ben")
        print("")
        print("")

    #  Recieving Name And Id From Admin

        print("Teacher's ID Viewer ")

        print("")

        teacherName = input("Teacher's Name : ").upper()

        print("")

        #  Obtaining Teacher's Table From Databse 

        sql.execute("use big_ben;")
        sql.execute("show tables")
        data = sql.fetchall()

        # Checking For Teacher's Name

        for i in data:
            a = i[0][0:7]

            if a == "teacher":
                sql.execute(f"select * from {i[0]}")
                teacherData = sql.fetchall()

                for j in teacherData:

                    if j[1] == teacherName:
                        print(f"{teacherName}'s ID is {j[0]}")
                        print("")
                        break
    
    else :
        print("! ! ! ! Please Shedule A Class To Use This Service  ! ! ! !")
        print("")