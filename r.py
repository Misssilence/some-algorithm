# This Python file uses the following encoding: utf-8
#正则表达式
#\d 一个数字 \w 一个字母或数字 .表示通配符 \s表示空格 {3}表示个数
#'-'是特殊字符，要转义 用\-
#*表示任意个， +表示至少一个
#P|p表示或， ^表示开头， $表示结束
#()使用括号可以进行分组匹配
#正则默认为贪婪匹配就是匹配尽可能多的，加个？就是非贪婪匹配
#汉字是[\u4e00-\u9fa5]
#1.邮箱正则

import re
mail = re.match(r'(^[0-9a-zA-Z\u4e00-\u9fa5])([0-9a-zA-Z_-]+)@([0-9a-zA-Z]+)\.(com|cn|cou)$', '我9-56550207@qq.com')
print(mail)

#2telephone r
telephone = re.match(r'^1[345678]\d{9}', '17816890354')
print(telephone)