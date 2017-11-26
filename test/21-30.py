# This Python file uses the following encoding: utf-8
#21实现方法isSortedAndHow，它接受一个整数数组，并返回下列结果之一：
    #
    # ‘yes, ascending’ 如果数组中的数字以升序方式排序
    # ‘yes，descending’ 如果数组中的数字以降序排列
    # ‘no’,如果不是上面任何一种排序就返回no;
    #用sorted来排序不错，返回一个新数组，并且原来的不变，顺便复习一下深拷贝
def is_sorted_and_how(arr):
    import copy
    old_arr = copy.deepcopy(arr)
    arr.sort()
    if old_arr == arr:
        return 'yes, ascending'
    arr.reverse()
    if old_arr == arr:
        return 'yes，descending'
    return 'no'
# print(is_sorted_and_how([3,2,1]))

#22 这个招式，要求对数字的每一位进行平方。
#
# 例如，如果我们通过该功能运行9119，811181将会出来。
#
# 注意：该函数接受一个整数并返回一个整数
def square_digits(num):
    arr = map(int, list(str(num)))
    new_arr = map(str, map(lambda x: x*x, arr))
    res_num = int(''.join(new_arr))
    return res_num
# print(type(square_digits(123)))

#23写一个函数，传入一个字符串作为参数，判断如果字符串是数字(0-9)，则返回true，否则返回false。
def is_digit(n):
    try:
        num = int(n)
        return True
    except:
        return False
# print(is_digit('a5'))

#24在这道招式中，你的任务是找到数组中第一个非连续的数字。
def first_non_consecutive(arr):

    for i in range(len(arr)-1):
        if arr[i+1] - arr[i] != 1:
            return arr[i+1]
    return None

# print(first_non_consecutive([1,2,3,4,6]))
#25真除数: 指某个数不包含该数字本身的除数
# 过剩数: 某个数的所有真除数之和,大于该数字本身
#
# 整数12是第一个这样的数字。它的真除数为1，2，3，4和6，相加的和为16（> 12）。
#
# 实现一个方法abundantNumber(num), 如果参数num是过剩数,则返回true,反之,返回false.
def abundant_number(num):
    num_arr = []
    for i in range(1, int(num / 2)+1):
        if num % i == 0:
            num_arr.append(i)
    if sum(num_arr) > num:
        return True
    return False
# print(abundant_number(37))

#25你的任务是实现一个函数(zebulansNightmare), 找到所有根据PEP8命名的函数,并将它们更改为驼峰式命名,例如：
def zebulansNightmare(functionName):
    str_arr = functionName.split('_')
    for i in range(1, len(str_arr)):
        str_arr[i] = str_arr[i].capitalize()
    return ''.join(str_arr)

# print(zebulansNightmare('main'))
#26给定2个字符串，你的任务是判断是否有一个子字符串同时出现在两个字符串。如果有，则返回true，否则返回false; 我们只考虑长度超过一个字母的子字符串。
def substring_test(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    if len(str1) > len(str2):
        find_str = str2
    else:
        find_str = str1
    for i in range(0, len(find_str)):
        for j in range(i+2, len(find_str)):
            if find_str[i:j] in str1 and find_str[i:j] in str2:
                return True
    return False
# print(substring_test("1234567","541265"))
# 27将字符串中的单词的末尾的所有感叹号删除。单词在字符串中用空格分开。
def remove(s):
    arr = s.split(' ')
    strip_arr = []
    for i in arr:
        if not "!"*len(i) in i:
            new_str = i.rstrip('!')
        else:
            new_str = i
        strip_arr.append(new_str)
    return ' '.join(strip_arr)
import re
def re_removes(s):

    return re.sub(r'\b!+', '', s)  #

def row_sum_odd_numbers(n):
    n_prev_num = sum([i for i in range(1, n)])
    return sum([2*i - 1 for i in range(n_prev_num+1,n_prev_num+n+1)])
# print(row_sum_odd_numbers(41))
def hex_to_dec(s):
    return int(s,16)
# print(hex_to_dec('10'))


def rank(st, we, n):
    if len(st) == 0:
        return 'No participants'
    rank_num = [sum([ord(i.lower())-96 for i in name])+len(name) for name in st.split(',')]
    for i in range(0, len(rank_num)):
        rank_num[i] = rank_num[i] *we[i]
    name_dict = dict(zip(rank_num, st.split(',')))
    new_rank_num = sorted(rank_num,reverse=True)
    print(name_dict)
    if len(new_rank_num) < n:
        return 'Not enough participants'
    return name_dict[new_rank_num[n-1]]

#28找到斐波那契数的最后一位数字
def get_last_digit(index):
    a, b = 0, 1
    n = 1
    while n < index:
        n += 1
        a, b = b, a + b
    return int(list(str(b))[-1])
# print(get_last_digit(79))


#29,组合一个新的数组
    # 从给定列表的第一个数字x开始,如果数字x小于3,则直接放到新的数组里面,然后继续下一个数字;
    # 如果数字x,大于等于3,则从x开始,后面的x个数字组成子数组,放到新的数组里面,然后从剩下的数字开始;
    # # 如果剩下的数字数量小于x,则返回剩下的所有
def unflatten(flat_array):

    new_arr = []
    length = len(flat_array)

    i = 0
    while i < length:
        if flat_array[i] < 3:
            new_arr.append(flat_array[i])
            i += 1
        else:
            num = flat_array[i]
            if i+num > length:
                extend_arr = [flat_array[i] for i in range(i, length)]
                new_arr.append(extend_arr)
                return new_arr
            else:
                extend_arr = [flat_array[i] for i in range(i, i+num)]
                new_arr.append(extend_arr)
                i += num
    return new_arr
#2.7 is to notice that use the i may be repeat
# print(unflatten([ 3, 5, 2, 1 ]))


#28实现一个函数sort_cards(),将杂乱无章的卡片,根据排名先后来排序,无论是数字还是字母;

# 所有的卡片上面的字母都是字符串,排序好的卡片列表如下所示:
def sort_cards(cards):
    str_arr = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    card_dict = dict(zip(str_arr, [i for i in range(1, 14)]))
    cards.sort(key=lambda x: card_dict[x])
    return cards
# print(sort_cards(list('39A5T824Q7J6K')))


#29,提取文件名文件名的格式：
    #
    # 以长串的数字开始；
    #
    # 其次就是下划线；
    #
    # 然后就是文件的扩展名；
    #
    # 在文件的扩展名后面总会跟着一个额外的扩展名；


def extract_file_name(dirty_file_name):
        import re
        return re.sub(r'(^\d+[_])|([.][a-zA-Z0-9]+$)', '', dirty_file_name)

# print(extract_file_name("1231231223123131_FILE_NAME.EXTENSION.OTHEREXTENSION"))

#30我妹妹放学回家做了这样一个课后作业：给一张方格纸，把它剪成一片一片的，然后组装它们， 使其形成的边为一个数字递增的序列。开始的时候很有趣，但是慢慢地，我已经厌倦了看到那堆被撕破的纸。所以我决定编写一个可以帮助解决问题同时也可以”保护树木节约资源”的程序。
# 任务
#
# 给定一个正整数n，返回一个严格递增的序列（取决于语言版本的列表/数组/字符串）数字，使得平方和等于n²。

def decompose(n):
    import math
    target = 2*n - 1
    list = [i**2 for i in range(1, int(math.sqrt(target))+1)]
    if target in list:
        return sorted([int(math.sqrt(target)), n-1])
    for i in range(len(list)-1):
        num = list[i]
        solve_list = [list[i], n-1]
        for j in range(i+1, len(list)):

            for tmp in range(j, len(list)):

                solve_list.append(list[tmp])
                num += list[tmp]

                if num == target:
                    return sorted(solve_list)
                elif num < target:
                    continue
                else:
                    num = list[i]
                    solve_list = [list[i], n-1]
                    break
    return 'Nothing'

#思路是 选定一个数字，然后加上下一个数字
#如果和等于目标就返回，如果<目标，就继续循环
def find_the_num(list, target):  #找出一个列表中，所有和为num的可能性

    for i in range(len(list)-1):
        num = list[i]
        solve_list = [list[i]]
        for j in range(i+1, len(list)):

            for tmp in range(j, len(list)):
                print(list[tmp])
                solve_list.append(list[tmp])
                num += list[tmp]

                if num == target:
                    return solve_list
                elif num < target:
                    continue
                else:
                    num = list[i]
                    solve_list = [list[i]]
                    break
    return 'Nothing'

# print(find_the_num([ 2, 3, 4, 5 ],10 ))


import re
s = re.match(r"^\+([1-9]\d) ([1-9]\d) ([1-9]\d{5})", "+12 34 567890")
# print(s.group(3))


def order_weight(strng):
    def sort_str(x, y):
        sub = sum(map(int, list(x)))-sum(map(int,list(y)))
        if not sub == 0:
            return sub
        return int(x[0])-int(y[0])
    weight_list = strng.split(' ')
    weight_list.sort(cmp=sort_str)


    return ' '.join(weight_list)

print(order_weight("103 123 4444 99 2000"))


# def order_weight(strng):
#     weight_list = strng.split(' ')
#     new_list = [sum(map(int, list(i))) for i in weight_list]
#     weight_dict = dict(zip(new_list, weight_list))
#
#     new_list.sort()
#     new_weight_list = [weight_dict[i] for i in new_list]
#
#     return ' '.join(new_weight_list)