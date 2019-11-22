
import pymysql
#链接数据库，用pycharm在数据库中，添加表，修改，删除等一系列操作

# 打开数据库连接
db = pymysql.connect("192.168.60.142", "root", "c123456", "student")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# sql1 = """CREATE TABLE zs1 (
#          FIRST_NAME  CHAR(20) NOT NULL,
#          LAST_NAME  CHAR(20),
#          AGE INT,
#          SEX CHAR(1),
#          INCOME FLOAT )"""
# cursor.execute(sql1)

# SQL 插入语句
sql = """INSERT INTO zs1(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000),('qwe','sss','50','s','5000')"""
try:
    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except:
    # 如果发生错误则回滚
    db.rollback()

# SQL 查询语句
sql = "SELECT * FROM zs1 \
       WHERE INCOME > %s" % (1000)
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 获取所有记录列表
   results = cursor.fetchall()
   for row in results:
      fname = row[0]
      lname = row[1]
      age = row[2]
      sex = row[3]
      income = row[4]
       # 打印结果
      print ("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
             (fname, lname, age, sex, income ))
except:
   print ("Error: unable to fetch data")

# SQL 删除语句
sql = "DELETE FROM zs1 WHERE AGE > %s" % (0)
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 提交修改
   db.commit()
except:
   # 发生错误时回滚
   db.rollback()



# 关闭数据库连接
db.close()