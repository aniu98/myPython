#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql

# 打开数据库连接
# db = pymysql.connect("10.114.12.15:3306", "root", "ab6gTsg3IIMjUP2S",
#                      "commission")


# 打开数据库连接
db = pymysql.connect(host="10.114.12.15",
                     user="root",
                     password="ab6gTsg3IIMjUP2S",
                     port=3306,
                     database="commission",
                     charset='utf8')
cursor = db.cursor()
sql = "SELECT * FROM resume"
print(sql)
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
        print("fname={},lname={},age={},sex={},income={}".format(
            fname, lname, age, sex, income))
except:
    print("Error: unable to fecth data")
print(db)
print(type(db))
