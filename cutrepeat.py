# This Python file uses the following encoding: utf-8
#去掉列表中的重复元素
l = ['1', '2', '2', '3', '4', '3', '5']
#1.set方法，利用set存储键，而且可以自动删去重复元素
'''
>>>print(list(set(l))) 
[1,2,3,4,5]
'''
#2 列表推导式
l2 = []
[l2.append(i) for i in l if i not in l2]
print(l2.index())

#fromkey可以创建一个新字典
# l2 = {}.fromkeys(l).keys()
# print(type(l2))
