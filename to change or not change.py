# This Python file uses the following encoding: utf-8

#修改字符串
#思想，现变成一个列表再改变
teststr = 'helli world'
# print(type(teststr))

#1
# tmp = []
# for i in teststr:
#     tmp.append(i)
# print(tmp)
# tmp[4] = 'o'
# endstr = ''.join(tmp)
# print(endstr)

# #默认参数的影响情况，默认参数为可变参数的时候
# class Stu():
#     def __init__(self, course=[]):
#         print(course)
#         self.course = course
#
#     def appcouse(self, course):
#         self.course.append(course)
#
#
# a = Stu()
# a.appcouse('english')
# a.appcouse('math')
# print(a.course)
#
# b = Stu()
# print(b.course)

#常用列表解析式,还有字典解析式，元组也可以元组这样就是一个生成器
# a = [2, 2, 3, 4, 5]
# b = [2, 2, 4, 5]
# c = (i for i in a if i not in b)
# print(next(c))
# print(next(c))


#
# import  time
# def report(when = time.time()):
#     print(when)
#
#
# def report2(when=time.time):
#     print(when)
# report()
# report2()