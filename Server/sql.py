# 导入pymysql模块
import pymysql
import json
list=["id","name","max","step"]
list2=["id","date","name","score"]
def sql_table(table):
    res=[]
    # 连接database
    conn = pymysql.connect(host='114.132.247.238', user='root',password='brysj123',database='lovelist',charset='utf8')
    # 得到一个可以执行SQL语句的光标对象
    cursor = conn.cursor()
    # 定义要执行的SQL语句
    sql = "select * from %s"%(table)
    try:
        cursor.execute(sql)  # 执行sql语句
        results = cursor.fetchall()  # 获取查询的所有记录
        # 遍历结果 #转为dict
        for i in range(0,len(results)):
            dict={list[0]:results[i][0],
                  list[1]:results[i][1],
                  list[2]:results[i][2],
                  list[3]:results[i][3]}
            res.append(dict)
        return res
    except Exception as e:
        raise e
    finally:
        conn.close()  # 关闭连接

def sql_name(name):
    res = []
    # 连接database
    conn = pymysql.connect(host='114.132.247.238', user='root', password='brysj123', database='lovelist',
                           charset='utf8')
    # 得到一个可以执行SQL语句的光标对象
    cursor = conn.cursor()
    # 定义要执行的SQL语句
    sql = "select * from %s" % (name)
    try:
        cursor.execute(sql)  # 执行sql语句
        results = cursor.fetchall()  # 获取查询的所有记录
        # 遍历结果 #转为dict
        for i in range(0, len(results)):
            dict = {list2[0]: results[i][0],
                    list2[1]: results[i][1].strftime('%Y-%m-%d'),
                    list2[2]: results[i][2],
                    list2[3]: results[i][3]}
            res.append(dict)
        return res
    except Exception as e:
        raise e
    finally:
        conn.close()  # 关闭连接

def sql_add(info):
    daily_dolist="daily_dolist"
    wyj_special_dolist="wyj_special_dolist"
    hrt_special_dolist = "hrt_special_dolist"
    # daily_dolist_dict 不同表的数据
    daily_dolist_dict={}
    special_dolist_dict={}
    people_name=""
    insert_data=[]
    #数据格式 info(id,score,daily,name)其中id为第几条要添加的记录，daily为日常否,name为表明（人名——
    if(info):
        people_name=info[0]["name"]
        res1=sql_table(daily_dolist)
        res2=sql_table(wyj_special_dolist)
        for i in res1:
            daily_dolist_dict[i["id"]]=i["name"]
        for i in res2:
            special_dolist_dict[i["id"]] = i["name"]
    for item in info:
        #先处理特殊
        if(item["daily"]==True):
            # print(item)
            # print(daily_dolist_dict)
            name=daily_dolist_dict[item["id"]]
            date=item["date"]
            score=item["score"]
        else:
            # 特殊的对象
            name=special_dolist_dict[item["id"]]
            date=item["date"]
            score=item["score"]
        cur=(date,name,score)
        # print("cur:"+cur)
        insert_data.append(cur)
    conn = pymysql.connect(host='114.132.247.238', user='root', password='brysj123', database='lovelist',
                           charset='utf8')
    # 得到一个可以执行SQL语句的光标对象
    cursor = conn.cursor()
    # 定义要执行的SQL语句
    sql = 'INSERT INTO '+people_name+'(date,name,score) values (%s,%s,%s)'
    try:
        cursor.executemany(sql,insert_data)  # 执行sql语句
        conn.commit()
        print("插入成功")

    except Exception as e:
        raise e
    finally:
        conn.close()  # 关闭连接



def sql_delete(info):
    sql = "delete from %s where id=%s;"%(info["name"],info["id"])
    conn = pymysql.connect(host='114.132.247.238', user='root', password='brysj123', database='lovelist',
                           charset='utf8')
    # 得到一个可以执行SQL语句的光标对象
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        conn.commit()
        print("删除成功")
    except Exception as e:
        raise e
    finally:
        conn.close()  # 关闭连接
    # 定义要执行的SQL语句
    return
# test='[{"id":1,"score":5,"daily":true,"name":"wyj","date": "2021-12-07"},{"id":2,"score":10,"daily":true,"name":"wyj","date": "2021-12-07"}]'
# test=json.loads(test)
# sql_add(test)



