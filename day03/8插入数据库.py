import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    port='3306',
    user='*****',
    password='*****',
    database='pabug',
    charset='utf8'
)

#设置游标
cur = conn.cursor()
#读取
with open('tencent.txt','r',encoding='utf-8',errors='ignore')as f:
    jobList = f.readlines()
    for job in jobList:
        job = eval(job)
        sql = "INSERT INTO tencent(jobName,jobStyle,jobArea,jobData) VALUES " \
              "(%r,%r,%r,%r)"%(job[0],job[1],job[2],job[3])

        print(sql)
        cur.execute(sql)
        conn.commit()

cur.close()
conn.close()