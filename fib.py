# This Python file uses the following encoding: utf-8
#斐波那契数列# 生活实际：1.走台阶问题，1次一个，或者两个，2.矩形面积问题

#  1 lambda :用lambda可以不用关注函数的形式，不需要确切的函数,利用递归的思想。
# '''
# >>>fib(2)
# 1
# >>>fib(4)
# 3
# '''

# fib = lambda n: 1 if n <= 2 else fib(n-1) + fib(n-2)


# 2 动态分配
'''
#fib : 0 1;1 2;2 3;
# 
# '''
def fib(n):
    a, b = 0, 1
    i = 1
    while i < n:
        a, b = b, a+b
        i += 1
    return b

# 3 yield 生成器

'''
>>>a = fib()



# '''
# def fib():
#     a, b = 0, 1
#     yield b
#     while True:
#         a, b = b, a+b
#         yield b


if __name__ == '__main__':
    print(fib(1))