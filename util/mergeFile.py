import os
path='E:/bak/'
filelist=os.listdir(path)

files=[]
for item in filelist:
    if '.sql' in item :
       files.append(item)

print(files)
newfile=open('E:/temp.sql','wb')
for item in files:
    print(path+item)
    for txt in open(path+item,'rb'):
        newfile.write(txt)

newfile.close()