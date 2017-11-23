# This Python file uses the following encoding: utf-8
#1. 1/2/3/4组成的不重复三位数
#A4取3 24种
def get_thenum():
    sum = 0
    for i in range(1, 5):
        for j in range(1, 5):
            for k in range(1, 5):
                if(i!=j and j!=k and i!=k):
                    print(100*i+10*j+k)
                    sum += 1
    print(sum)


#2.企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
#   利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
#   20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于
# 　40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，
#   高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
#   1.程序分析：请利用数轴来分界，定位。注意定义时需把奖金定义成长整型。　
award1 = 10*0.1
award2 = award1 + 10*0.075
award3 = award2 + 20*0.05
award4 = award3 + 20*0.03
award5 = award4 + 40*0.015
def get_award():
    profit = int(input('请输入当月利润(单位为W):'))
    if profit <= 10:
        award = profit*0.1
    elif profit <= 20:
        award = award1 + 0.075*(profit-10)
    elif profit <= 40:
        award = award2 + 0.05*(profit-20)
    elif profit <= 60:
        award = award3 + 0.03*(profit-40)
    elif profit <= 100:
        award = award4 + 0.015*(profit-60)
    else:
        award = award5+0.01*(profit-100)
    print('当月奖金为%sW' % award)
    return award

#3题目：一个整数，它加上100后是一个完全平方数，再加上268又是一个完全平方数，请问该数是多少？
# 1.程序分析：在10万以内判断，先将该数加上100后再开方，再将该数加上268后再开方，如果开方后
# 　　　　　　的结果满足如下条件，即是结果。请看具体分析：
import math
def choose_thesquare(n):
    n_square = int(math.sqrt(n))
    if n_square *n_square == n:
        return True
    return False

def get_square_num(n):
    for i in range(n+1):
        if(choose_thesquare(i+100) and choose_thesquare(i+368)):
            print(i)
            return i
    print('不存在相应数字')

#4输入某年某月某日，判断这一天是这一年的第几天？
# 1.程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊
# 　　　　　　情况，闰年且输入月份大于3时需考虑多加一天。
import re

def judge_leap_year(n):
    if n % 400 == 0:
        return True
    elif n % 4 == 0 and n % 100 != 0:
        return True
    return False

def get_theday():
    data_input = input('请输入日期，格式为（xx-xx-xx）:')
    while 1:
        if not re.match(r'^(\d+)-(\d{1,2})-(\d{1,2})$', data_input):
            print('请重新输入')
            data_input = input('请输入日期，格式为（xx-xx-xx）:')
        else:
            break
    data = data_input.split('-')#也可以用re.match.group
    month_day = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]#月的前几个月份的天数

    year = int(data[0])
    month = int(data[1])
    day = int(data[2])

    if month > 12 or day > 31:
        raise ValueError('输入月份错误或日期错误')

    if judge_leap_year(year) and month >= 3:
        print('这是%s年的第%s天' %(year, (month_day[month-1]+day+1)))
    else:
        print('这是%s年的第%s天' %(year, (month_day[month-1]+day)))

#5题目：输入三个整数x,y,z，请把这三个数由小到大输出。
# 1.程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，
# 　　　　　　然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。
def output_small(n):
    seq = []
    for i in range(n):
        x = int(input('请输入第%s个数字:' %(i+1)))
        seq.append(x)
    #选择排列
    for i in range(0, len(seq)-1):
        index = i
        for j in range(i+1, len(seq)):
            if seq[j] < seq[index]:
                index = j
            seq[i], seq[index] = seq[index], seq[i]
    print(seq)

#6题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月
# 　　　后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
# 1.程序分析：　兔子的规律为数列1,1,2,3,5,8,13,21....
# 2.程序源代码：（fib）
def fib(n):
    a, b = 0, 1
    i = 1
    print(b)
    while i < n:
        a, b = b, a+b
        i += 1
        print(b)


#7多重继承和super
class A(object):
    def __init__(self):
        print('A')

class B(A):
    def __init__(self):
        super(B, self).__init__()
        print('B')
class C(A):
    def __init__(self):
        super(C, self).__init__()
        print('C')
class D(C,B):
    pass
#
# e = D()  #A,B,C super不是指父类，而是mro中的下一个类，这样实现了广度优先，并且确保每个类只被调用一次
# print(e.__class__.mro())


#8.将一个正整数分解质因数
#n从2开始到原数字,采用递归不断分解
prime_seq = []
from functools import reduce
def prime_factors(n):
    origin_data = n
    if origin_data > 2:
        for i in range(2, n+1):
            if origin_data % i == 0:
                prime_seq.append(i)
                origin_data = int(origin_data/i)
                return prime_factors(origin_data)
    # print('%s=','*'.join(prime_seq) %n)
    a = map(str, prime_seq)
    print('*'.join(a), '=', reduce(lambda x, y: x*y, prime_seq))

#9题目：打印出所有的“水仙花数”，所谓“水仙花数”是指一个三位数，其各位数字立方和等于该数
# 　　　本身。例如：153是一个“水仙花数”，因为153=1的三次方＋5的三次方＋3的三次方。
# 1.程序分析：利用for循环控制100-999个数，每个数分解出个位，十位，百位。
# 2.程序源代码：
def shuixianhua(n):
    for num in range(100, n):
        i = int(num / 100)
        j = int(num / 10) % 10
        k = num-100*i-10*j

        if i**3+j**3+k**3 == num:
            print(num)

import cProfile
import sys
#10,判断101-200之间有多少个素数，并输出所有素数。
def run_prime():
    for i in range(101, 100000):

        for num in (2, i/2):
            if i % num == 0:
                break
            else:
                sys.stdout.write(str(i))

if __name__ == '__main__':
    # get_thenum()
    # get_award()
    # get_square_num(100000)
    # print(judge_leap_year(2000))
    # get_theday()
    # output_small(5)
    # prime_factors(1000)
    # shuixianhua(10)
    cProfile.run('run_prime()')