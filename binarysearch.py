# This Python file uses the following encoding: utf-8
#二分查找

def binarySearch(l, target):
    bottom = 0
    top = len(l) - 1

    while top >= bottom:
        middle = (top + bottom) // 2
        if target == l[middle]:
            return middle
        elif target > l[middle]:
            bottom = middle + 1
        else:
            top = middle - 1
    return('%s is not in this list' %target)

def power_x(x, n):
    if n == 1:
        return x
    if n % 2 == 0:
        return power_x(x, n/2)*power_x(x, n/2)
    return power_x(x, (n-1)/2)*power_x(x, (n-1)/2)*x

def power_x2(x, n):
    if n==0:
        return 1
    return power_x(x, n-1)*x

import cProfile
cProfile.run('power_x(3,1000000)')
cProfile.run('power_x2(3,1000000)')


if __name__ == '__main__':
    print(binarySearch([], 5))
    # l = ['11', '233', '-444', '0', '3']
    # l.sort(key=lambda x : int(x))
    # print(l)
