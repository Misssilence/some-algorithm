# This Python file uses the following encoding: utf-8
#首先关于普通的赋值，普通的赋值其实就是地址的传递，两者是一样的
#例如
# a = 2
# b = a
# print(id(a)) #" 161..."
# print(id(b)) #"161...."
#而浅拷贝，也就是普通的copy
from copy import copy
# a = [1, 'man', ['1', '2']]
# b = copy(a)
#
# b[2].append(3)
# b[0] = 3
# print(a, b)
a = [0, 0, 0, [1,2]]
b = copy(a)
print(id(a[3]))
print(id(b[3]))
b[3].append(3)
print(a[3])
print(b[3])
print(id(a[3]))
print(id(b[3]))
# print(id(a[0]))
# print(id(b[0]))
# print(a[2])
# print(b[2])
# print(b[0])
#两者是 不一样的对象，但是里面的元素的地址是一样的，也就是里面的内容一样
#而深拷贝，就是完全不一样，只不过两者的值相同，地址完全不一样，所以深拷贝的拷贝对象怎么变化都不会影响它。