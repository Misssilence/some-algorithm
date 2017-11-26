# This Python file uses the following encoding: utf-8
#11利用递归方法求5!。
def jiecheng(n):
    if n==1:            #递归终止条件
        return 1
    return n*jiecheng(n-1)  #n和n-1的关系


from functools import reduce
#12求1+2!+3!+...+20!的和
def op(n):
    sum_seq = []
    for i in range(1, n+1):
        sum_seq.append(i)
    print(sum(map(jiecheng, sum_seq)))
    # s =reduce(sum, sum_seq)
    # print(s)
#13,有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
itm1 = 2
itm2 = 1
sum_seq = []
for i in range(3):
    itm = itm1/itm2
    sum_seq.append(itm)
    itm1, itm2 = itm1+itm2, itm1
# print(sum(sum_seq))


#14给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
def new_avg(arr, newavg):
    num_person = len(arr)
    total = newavg * (num_person+1)
    next_money = total - sum(arr)
    if next_money <= 0:
        raise ValueError('The nexavg is error')
    return next_money
#
#
# print(new_avg([1,2,3,4], 2))

def obfuscate(email):
    new_email = email.replace('.', '[dot]')
    new_email = new_email.replace('@', '[at]')
    return new_email

# print(obfuscate('122@33.'))

#15一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
def get_the_circlenum(num):
    num_1 = int(num/10000)
    num_2 = int(num/1000) % 10
    num_4 = int(num/10) % 10
    num_5 = num % 10
    if num_1 == num_5 and num_2 == num_4:
        print(num)
    else:
        print('No')

#16
def alternate_sq_sum(arr):
    if arr == []:
        return 0
    sum_new_arr = sum(map(lambda x: x * x, arr[::2]))
    return sum(arr[1::2]) + sum_new_arr

#17格式化小数点后面的数字#1
def two_decimal_places(number):
    if not isinstance(number, float):
        raise NotImplementedError("TODO: two_decimal_places")
    num_str = str(number).split('.')
    num_dot_str = num_str[1][:2]
    return float(num_str[0]+'.'+num_dot_str)

#18leetspeak
def to_leet_speak(str):
    leet_dict={
  'A' : '@',
  'B' : '8',
  'C' : '(',
  'D' : 'D',
  'E' : '3',
  'F' : 'F',
  'G' : '6',
  'H' : '#',
  'I' : '!',
  'J' : 'J',
  'K' : 'K',
  'L' : '1',
  'M' : 'M',
  'N' : 'N',
  'O' : '0',
  'P' : 'P',
  'Q' : 'Q',
  'R' : 'R',
  'S' : '$',
  'T' : '7',
  'U' : 'U',
  'V' : 'V',
  'W' : 'W',
  'X' : 'X',
  'Y' : 'Y',
  'Z' : '2'
    }
    new_str = str
    for i in str:
        if not i.isspace():
            new_str = new_str.replace(i, leet_dict[i])
    print(new_str)
    return new_str

#19 给你一个数组,找出该数组里面的所有奇数,并计算所有奇数的立方和;如果任何值都不是数字，这个函数将返回undefined。
def cube_odd(arr):
    str_arr = [i for i in arr if isinstance(i, str)]
    new_arr = [i for i in arr if isinstance(i, int) and i % 2 != 0]
    if len(str_arr) > 0:
        return None
    return sum(map(lambda x: x*x*x, new_arr))
#还可以用try，except 来报错

#20.给你一个数字56789,将这个数字向左旋转得到:67895;
# 将上述得到的数字保留一位数,然后向左旋转得到:68957;
# 将上述得到的数字保留两位数,然后向左旋转得到:68579;
# 将上述得到的数字保留三位数,然后向左旋转得到:68597;
#
# 事实上,你不需要在进行保留四位数字进行旋转了,因为保留四位数字,就剩下一位数字了,本身就是最大的;
#返回旋转过程中的最大数字
def max_rot(n):
    max = n
    arr = list(str(n))
    for i in range(len(arr)-1):
        arr.append(arr.pop(i))
        if int(''.join(arr)) > max:
            max = int(''.join(arr))
    return max

# #20 你有一个从1开始的正数序列，但是其中有一个数字是缺失的！
#
# 找出缺失的数字,并返回; 如果序列没缺失数字，你应该返回0
#
# 简而言之，一个无效的序列（一个非数字字符串）必须返回1，一个正确的无缺的序列必须返回0; 缺失多于一个数字的序列应该返回最小的缺失数字; 缺失一个数字则返回缺少的号码。
#
# 请注意，输入可能是随机的顺序。
def find_missing_number(sequence):
    if sequence == '':
        return 0
    try:
        seq = map(int, sequence.split(' '))
        num_seq = [i for i in seq if isinstance(i, int)]
        complete_seq = [i for i in range(1, max(num_seq)+1)]
        lost_seq = [i for i in complete_seq if i not in num_seq]
        if len(lost_seq) == 0:
            return 0
        return min(lost_seq)
    except:
        return 1

print(find_missing_number(" "))
if __name__ == '__main__':
    # print(jiecheng(5))
    # op(3)
    get_the_circlenum(14541)
    # print(two_decimal_places(10.24))
    to_leet_speak('LEET')