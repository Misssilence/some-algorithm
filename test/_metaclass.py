#python 当中一切都是对象，类也是对象
#可以利用type来创建类
#而使用metaclass的时候，在创建类的时候就会自动传入类名，继承的父类和含有的参数到做为元类创建类的地方
#然后利用传入进来的这几个参数，就是type创建类所需要的参数来创建类，可以在创建类的时候进行一些修改
aa = type('aaa', (), {'add': 123})
# a = aa()
# print(a.__class__.__name__)
# print(aa)
import six
@six.add_metaclass
class ListMetaclass(type):
    def __new__(cls, name, bases, attr):
        '''

        :param name:类名
        :param bases: 继承父类
        :param attr: 类含有参数
        :return:
        '''
        print(name)

        return type.__new__(cls, name,bases, attr)

__metaclass__ = ListMetaclass

class a():
    __metaclass__ = ListMetaclass
    c = 'llala'
    print('end')
    pass
print('start')
class b(a):
    pass

# print(a.__class__, b.__class__,a.__bases__, b.__bases__)
#使用实例比如说orm进行对应
#可以创建一个元类，然后如果是一个modle就直接返回类，
# 而如果类名不是model就可以将里面的attr进行对应数据库
from abc import ABCMeta
# abstract base classes 一个生成抽象类的元类
#抽象类是据有一个或多个抽象方法的类，必须声明为抽象类。
# 抽象类的特点是，不能创建实例。
#实现的方法就是如果存在抽象方法就不能实例
from abc import ABCMeta, abstractmethod

#抽象类
# class Headers(object):
#     __metaclass__ = ABCMeta
#
#     def __init__(self):
#         self.headers = '3333'
#
#     @abstractmethod
#     def _getBaiduHeaders(self):
#         pass
#
#     def __str__(self):
#         return str(self.headers)
#
#     def __repr__(self):
#         return repr(self.headers)
#
# #实现类
# class BaiduHeaders(Headers):
#     # def __init__(self, url, username, password):
#     #     self.url = url
#     #     self.headers = self._getBaiduHeaders(username, password)
#
#     # def _getBaiduHeaders(self, username, password):
#     #
#     #     pass
#     pass
#
# a = BaiduHeaders()
# print(a.__repr__)

# class A(metaclass=ABCMeta):
#     # __metaclass__ = ABCMeta
#
#     # @abstractmethod
#     def a(self):
#         pass
#
# class B(A):
#     @abstractmethod
#     def c(self):
#         pass
#
#
# # c = A()
# d = B()

# class All_file(metaclass=ABCMeta):
#     all_type='file'
#     # __metaclass__ = ABCMeta
#     @abstractmethod #定义抽象方法，无需实现功能
#     def read(self):
#         '子类必须定义读功能'
#         pass
#
#     @abstractmethod #定义抽象方法，无需实现功能
#     def write(self):
#         '子类必须定义写功能'
#         pass
#
# class Txt(All_file):
#     pass
# a = All_file()
# t1=Txt() #报错,子类没有定义抽象方法

# class MaterialObserver():
#     """
#     观察者模式：意图相关素材观察者，具体素材类进行继承
#     """
#     __metaclass__ = ABCMeta
#
#
#
#
#     @abstractmethod
#     def query(self, *args, **kwargs):
#         """
#         请求推荐接口，子类需覆盖该方法
#         :param args:
#         :param kwargs:
#         :return:
#         """
#         raise NotImplementedError
#
# # C = MaterialObserver()
# # C.query()
#
# import abc
# from abc import abstractmethod
#
# class Sheep(object, metaclass=ABCMeta):
#     @abstractmethod
#     def a(self):
#         pass
# class a(Sheep):
#     def a(self):
#         pass


# c = a()
