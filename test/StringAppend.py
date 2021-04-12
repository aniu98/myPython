# 1 来自C语言的%方式

print('%s %s' % ('Hello', 'world'))


# 2、format()拼接方式
test="test"
test2="test2"
print("append is {}, {} ".format(test,test2))

# 3、() 类似元组方式

s_tuple = ('Hello', ' ', 'world')
s_like_tuple = ('Hello' ' ' 'world')
print(s_tuple)
print(s_like_tuple)

# 4、面向对象模板拼接
from string import Template
s = Template('${s1} ${s2}!') 
print(s.safe_substitute(s1='Hello',s2='world')) 
# 5、常用的+号方式
print("hello"+ "word")


# 7、f-string方式
print(f'Hello {test}. My name is {test2}.')

print(f"Hello {test}. My name is {test2}.")
