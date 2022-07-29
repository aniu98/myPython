#!/usr/bin/python
# -*- coding: UTF-8 -*-
# pip install docxtpl
from docxtpl import DocxTemplate, RichText
import shutil
import os
import sys
import difflib

version='1.0.5.0'
lastVersion='1.0.4.0'
author="阿牛"
baseDir='/提测文档/'

destFilePath =baseDir+"前台应用-V"+version+"/"
if not(os.path.exists(destFilePath)):
    os.makedirs(destFilePath)
applicationSrcYml="./template/application.yml"
applicationDestYml=destFilePath+"application.yml"
shutil.copy(applicationSrcYml, applicationDestYml)

lastVersionYml=baseDir+"前台应用-V"+lastVersion+"/"+'application.yml'
file1 = open(lastVersionYml,'r',encoding='UTF-8').readlines()
file2 = open(applicationSrcYml,'r',encoding='UTF-8').readlines()
# diff = difflib.ndiff(file1, file2)
# sys.stdout.writelines(diff)
d = difflib.Differ()
list1 = list(d.compare(file1,file2))

rt=RichText("")
for line in list1:
    if line[0] == "?": list1.remove(line) 
    if line[0] == '-': rt.add(line.replace('-','',1), strike=True)
    if line[0] == '+': rt.add(line.replace('+','',1), color='#ff0000')
    if line[0] == ' ': rt.add(line.replace(' ','',1))
# with open(destFilePath+"diff.yml", 'w') as file_object:
#     # file_object.write(list1)
#     for line in list1:
#         # file_object.write("\n")
#         file_object.write(line)
data_dic = {
'version': version,
"author":author,
"year":2020,
"month": 8,
"day":31,
'yml':rt,
'apinNum':167
}

print(data_dic)
templateFileName="安装升级手册.docx"
doc = DocxTemplate('./template/'+templateFileName) #加载模板文件
doc.render(data_dic) #填充数据
doc.save(destFilePath+templateFileName.replace('version',version)) #保存目标文件

templateFileName='应用部署手册.docx'
doc = DocxTemplate('./template/'+templateFileName) #加载模板文件
doc.render(data_dic) #填充数据
doc.save(destFilePath+templateFileName.replace('version',version)) #保存目标文件