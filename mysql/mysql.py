#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql
from docxtpl import DocxTemplate
# 打开数据库连接
db = pymysql.connect(host="10.114.12.15",user="root",password="ab6gTsg3IIMjUP2S",port=3306,database="commission",charset='utf8')
cursor = db.cursor()
sql = "SELECT identityNum,name,sex,level,position,birthday,school,education,major,yearsOfExperience,currentPosition,expectPosition,skill,idCardImgFront,idCardImgBack FROM resume "
sql = sql + " where identityNum in ('1')"
list=[]
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    resumes = cursor.fetchall()
    for row in resumes:
        person = {"identityNum": row[0], "name": row[1], "sex": row[2], "level": row[3], "position": row[4], "birthday": row[5], "school": row[6], "education": row[7],
                  "major": row[8], "yearsOfExperience": row[9], "currentPosition": row[10], "expectPosition": row[11], "skill": row[12], "idCardImgFront": row[13], "idCardImgBack": row[14]}
        
        # 工作经验
        sql = "select startDate,endDate,company,workCompany,description,duty from resumeExperience where identityNum= '" + \
            person["identityNum"]+"'"
        print(sql)
        cursor.execute(sql)
        resumeExperiences = cursor.fetchall()
        person["resumeExperiences"]=[]
        for row in resumeExperiences:
            experience = {"startDate": row[0], "endDate": row[1], "company": row[2],
                          "workCompany": row[3], "description": row[4], "duty": row[5]}
            person["resumeExperiences"].append(experience)
        # 教育经历
        sql = "select education,degree,startDate,endDate,graduationCertificateImg from resumeEducation where identityNum= '" + \
                person["identityNum"]+"'"
        print(sql)
        cursor.execute(sql)
        resumeEducations = cursor.fetchall()
        person["resumeEducations"] = []
        for row in resumeEducations:
            experience = {"education": row[0], "degree": row[1], "startDate": row[2],
                          "endDate": row[3], "graduationCertificateImg": row[4]}
            person["resumeEducations"].append(experience)

        # 打印结果
        print(person)
        list.append(person)
except:
    print("Error: unable to fecth data")

doc = DocxTemplate("resume.docx")
for person in list: 
    doc.render(person)
    doc.save("generated_doc.docx")


