#!/usr/bin/python
# -*- coding: UTF-8 -*-

import base64
import os

isEncodeFlag= True # 是否转成base64 标识
# isEncodeFlag= False
# 把文件转成 base64	
def encodeFile(fileName):
	if ".py" not in fileName and ".base64" not in fileName:
		file = open(fileName,"rb").read()
		encodeStr = base64.b64encode(file)
		tFile = open(fileName+".base64","w+")
		tFile.write(fileName+";"+str(encodeStr))
		tFile.close()
		print("encodeFile success: "+ fileName)
#把.base64 文件进行 decode
def decodeFile(fileName):
	if ".base64" in fileName:
		text = open(fileName).read().split(";")
		jarFile = open(text[0],"wb+")
		jarFile.write(base64.b64decode(text[1]))
		jarFile.close()
		print("decodeFile success: "+fileName)
# main
# fileNames = os.listdir(os.path.abspath('.'))
fileNames = [name for name in os.listdir(os.path.abspath('.')) 
        if os.path.isfile(os.path.join(os.path.abspath('.'), name))]
print(fileNames)
if isEncodeFlag:
	for fileName in fileNames:
		encodeFile(fileName)
else :
	for fileName in fileNames:
		decodeFile(fileName)
