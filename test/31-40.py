# This Python file uses the following encoding: utf-8
#31 计算给定范围内的素数对的总数，具有以下属性：素数对数字的乘积之和也是素数。

# 注意:区间的上限不会超过10000。区间(0,10)意思是：0 <= n < 10。
def check_prime(n):
    if n == 1 or n == 0:
        return None
    for i in range(2, n):
        if n % i == 0:
            return None
    return n

def solve(a,b):
    from functools import reduce
    import math
    prime_arr = [i for i in range(a, b+1) if check_prime(i)!=None]

    sum = 0
    for i in range(len(prime_arr)):
        for j in range(i, len(prime_arr)):
            num_list = map(int, list(str(prime_arr[i]*prime_arr[j])))
            res = reduce(lambda x, y: x+y, num_list)
            if check_prime(res) != None:
                sum += 1
    return sum


# print(solve(2,2000))


#计算烂橘子，每个烂橘子会每一小时会腐蚀相邻的橘子腐烂的桔子会腐蚀每一个相邻的桔子

# 我们会以一个数组(包含两个子数组)来代表一箱桔子
#
# 2 表示烂桔子
#
# 1 表示新鲜桔子
#
# 0 表示空

#32破解凯撒加密
import requests
from lxml import etree

alpha_arr = ['hello', 'world', 'wtf', 'fox', 'quick','the', 'brown','jumps', 'over', 'the', 'lazy', 'dog']
def spider(url):
    data_item = requests.get(url)
    data_item.encoding = 'utf-8'
    selector = etree.HTML(data_item.text)
    alpha_list = selector.xpath('//*[@id="cr"]/div[1]/div[5]/div[1]/p/text()')

    for i in alpha_list:
        a = i.split('、')
        if len(a) >1 :
            alpha = a[1].split()[0]
            if alpha.isalpha():
                alpha_arr.append(alpha)
for page in range(1, 5):
    url = 'http://cet4.koolearn.com/20170927/81755'+str(page)+'.html'
    # spider(url)

def break_caesar(message):
    for shift in range(1, 26):
        new_message_arr = []
        for i in message:
            if (ord(i)>=65+shift and ord(i)<=90) or (ord(i)>=97+shift and ord(i)<=122):
                new_message_arr.append(chr(ord(i)-shift))
            elif(ord(i)>=65 and ord(i)<65+shift) or (ord(i)>=97 and ord(i)<97+shift):
                new_message_arr.append(chr(ord(i)+26-shift))
            else:
                new_message_arr.append(chr(32)) #把所有其他字符变成空格


        new_message= ''.join(new_message_arr)
        words = new_message.split()
        words = [i.lower() for i in words]
        check_words = [i for i in words if i in alpha_arr]
        if check_words == words:
            return shift

# print(break_caesar("Mjqqt, btwqi!"))
