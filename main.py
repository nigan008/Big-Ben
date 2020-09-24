import time 

import pymysql
conn=pymysql.connect(host="localhost",user="root",password="",db="project")
a=conn.cursor()

""" sql ="insert into std_12 values(%s,%s,%s,%s,%s,%s,%s);"
val=['SUPW','1','NTR','NTR','NTR','NTR','NTR']
a.execute(sql,val) """

teachers = []
noOfSection = 5
a.execute("select * from std_12")

"""data =a.fetchone()
for i in data:
    print(i) """

def sorting():
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
sorting()
for s in teachers :
    print(s)
time.sleep(5)
