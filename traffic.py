# 交通票生成
from calendar import month
from cgi import test
import random
import time
import numpy as np

year=2022
month=7,7
total =8100
moneyRange=280,300
a1=(year,month[0],1,0,0,0,0,0,0)       #设置开始日期时间元组（1976-01-01 00：00：00）
a2=(year,month[1],31,23,59,59,0,0,0)  #设置结束日期时间元组（1990-12-31 23：59：59）


a= random.sample(range(2,100),8)
print(a)


start=time.mktime(a1)  #生成开始时间戳
end=time.mktime(a2)   #生成结束时间戳
#随机生成10个日期字符串
for i in range(32):
  t=random.randint(start,end)  #在开始和结束时间戳中随机取出一个
  date_touple=time.localtime(t)     #将时间戳生成时间元组
  date=time.strftime("%Y-%m-%d",date_touple) #将时间元组转成格式化字符串（1976-05-21）
  print(date)

calc = True
list =[]
sum=0
while calc:
    l =random.sample(range(moneyRange[0],moneyRange[1]),1)
    list.append(l[0])
    sum=sum+l[0]
    calc= sum<total
print(list,sum)