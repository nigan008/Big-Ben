import pymysql
conn=pymysql.connect(host="localhost",user="root",password="",port = 3308)
sql=conn.cursor()

print("")
print("                                Teacher's ID Viewer ")
print("")
teacherName = input("                  Teacher's Name : ")
print("")
sql.execute("use big_ben;")
sql.execute("show tables")
data = sql.fetchall()

for i in data:
    a = i[0][0:7]
    if a == "teacher":
        sql.execute(f"select * from {i[0]}")
        teacherData = sql.fetchall()
        for j in teacherData:
            if j[1] == teacherName:
                print(f"                  {teacherName}'s ID is {j[0]}")
                break
        break
