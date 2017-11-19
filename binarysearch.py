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

if __name__ == '__main__':
    print(binarySearch([], 5))
    # l = ['11', '233', '-444', '0', '3']
    # l.sort(key=lambda x : int(x))
    # print(l)
