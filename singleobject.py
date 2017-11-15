# This Python file uses the following encoding: utf-8

#单例模式，只有一个实例对象，比如在cocos2d开发当中，事件分发实例就是一个单例对象，这样就不会出现实例的冲突

#1.利用字典存储，__new__
class SingleObject(object):
    _singledog = {}
    def __new__(cls, *args, **kwargs):
        if not cls in cls._singledog:
            cls._singledog[cls] = super(SingleObject, cls).__new__(cls, *args, **kwargs)
        return cls._singledog[cls]

#2.利用类装饰器
def Single(cls,*args, **kwargs):
    _singledog = {}
    def singledog():
        if not cls in _singledog:
            _singledog[cls] = cls(*args, **kwargs)
        return _singledog[cls]
    return singledog


@Single
class A:
    pass


if __name__ == '__main__':
    a = []
    print(id(a))
    def hi(a):
        a.append(1)
        return a
    print (id(hi(a)))