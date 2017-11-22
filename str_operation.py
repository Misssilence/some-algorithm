# This Python file uses the following encoding: utf-8
str = ' i love  you '
#1.字符串去空格，字符
str1 = str.strip().lstrip('i')
# print(str1)
#2字符串截取
str2 = str[1:4]
print(str2)

#3字符串查找
print(str.find('i'))
# print(str.index('love'))

#如果是子字符串建议用in来查找
print('i' in str1)
#4字符串替换
print(str.replace('i', 'y', 1)) #不指定count就是默认值-1，全部都替换

#5字符串分割
strlist = str.split(' ') #前者制定了分割的符号，就会把1个空格进行分割，而下一个没有指定就将多个空格当成，并且会去掉首尾空格
strlist1 = str.split()
# print(strlist)
# print(strlist1)
#还可以用rstrip 进行正则切割