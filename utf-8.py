
info = '\xe9\x95\xbf\xe6\xb2\x99\xe8\xa5\xbf\xe7\x89\x87\xe5\x8c\xba-\xe9\x87\x91\xe7\xa7\x91\xe4\xb8\x93\xe7\xbd\x91-\xe9\x80\x9a\xe7\x94\xa8\xe4\xb8\x9a\xe5\x8a\xa1\xe5\x9f\x9f' #字符串类型

# out = bytes(info,'utf-8').decode('unicode_escape').encode('latin1').decode()

# print(out)


info = info.encode('unicode_escape').decode('utf-8')
out = bytes(info,'utf-8').decode('unicode_escape').encode('latin1').decode()
print(out)