#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名: test.py
import base64
import sys
import os
print(sys.argv[0])
print (os.getcwd())#获得当前目录
print (os.path.abspath('.'))#获得当前工作目录
print (os.path.abspath('..'))#获得当前工作目录的父目录
print (os.path.abspath(os.curdir))#获得当前工作目录

#sys.argv[1]

fileNames = os.listdir(os.path.abspath('.'))
print(fileNames)

for fileName in fileNames:
	pass
	print( "test")
	
for i in range(len(fileNames)):
   print 'var :', fileNames[i]

if False:
	sFile = open("helloWord.py","rb").read()
	encodeStr = base64.b64encode(sFile)
	tFile = open("base64","w+")
	tFile.write(str(encodeStr))
	tFile.close()
	print("success")
elif False:
	print("test elif")
else :
	text = open("base64").read()
	#print text
	jarFile = open("aniu.py","wb+")
	jarFile.write(base64.b64decode(text))
	jarFile.close()
	print "success"