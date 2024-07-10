import pymysql
connection = pymysql.connect(host='localhost',
                             user='root',
                             passwd='0000',
                             database='mydb',
                             charset='utf8')
#有条件查询
try:
    with connection.cursor() as cursor:                           #建立游标
        sql = 'select name,userid from user where userid>%(id)s'  #查询语句
        cursor.execute(sql, {'id': 0})                       #执行查询语句，绑定参数
        result_set = cursor.fetchall()                            #提取结果选择集
        for row in result_set:                                    #遍历结果
            print('id:{0} - name:{1}'.format(row[1],row[0])) #输出
finally:
    connection.close()                                           #关闭


'''
#无条件查询
try:
    with connection.cursor() as cursor:         #建立游标
        sql = 'select max(userid) from user '   #查询语句
        cursor.execute(sql)                     #执行语句，绑定参数

        row = cursor.fetchone()                 #提取所有结果集
        print(row)

        if row is None:
            print('最大用户id:(0)'.format(row[0]))
finally:
    connection.close()
    
'''
#查
with connection.cursor() as cursor:
    sql='select * from user'
    cursor.execute(sql)
    result=cursor.fetchall()
    for row in result:
        print(row)
#增
with connection.cursor() as cursor:
    sql = 'insert into user (name,userid) values("John2",4)'
    cursor.execute(sql)
    sql2 = 'select * from user'
    cursor.execute(sql2)

    result = cursor.fetchall()
    for row in result:
        print(row)
#增多行数据
with connection.cursor() as cursor:
    sql = 'insert into user (name,userid) values("Bob",5),("JB",6)'
    cursor.execute(sql)
    sql2 = 'select * from user'
    cursor.execute(sql2)

    result = cursor.fetchall()
    for row in result:
        print(row)
 #删
with connection.cursor() as cursor:
    sql = 'delete from user where userid=2'
    cursor.execute(sql)
    sql2 = 'select * from user'
    cursor.execute(sql2)

    result = cursor.fetchall()
    for row in result:
        print(row)
#改
with connection.cursor() as cursor:
    sql = 'update user set userid=1 where name ="John"'
    cursor.execute(sql)
    sql2 = 'select * from user'
    cursor.execute(sql2)

    result = cursor.fetchall()
    for row in result:
        print(row)