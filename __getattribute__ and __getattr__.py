# This Python file uses the following encoding: utf-8
class a(object):

    def __init__(self, name):
        self.name = name

    # def __getattribute__(self, item):
    #
    #     print('hi')
    #
    # def __getattr__(self, item):
    #     print(item)
    def __add__(self, other):
        print('xiangjia', other)
#这两个都是在实例对象调用属性的时候调用，下一个只在不含有这个实例的时候调用
b = a('paca')

print(b.name)
'''
>>>b + 'aaccddc'
xiangjia aaccddc
'''
# print(b.what)
