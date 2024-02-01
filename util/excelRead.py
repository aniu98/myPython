import codecs
path="C:\\Users\\admin\\Downloads\\test"


# 指定使用utf-8字符集读取文件内容
f = codecs.open(path, 'r', 'utf-8', buffering=True)
# 使用readlines()读取所有行，返回所有行组成的列表
for i in f.readlines():
    print(i, end='')
f.close()