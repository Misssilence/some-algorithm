# This Python file uses the following encoding: utf-8
#快速重排，任选一个，那就第一个吧，然后选出比它大的，继续重排，小的继续重排

def qsort(seq):
    if seq == []:
        return []
    else:
        tmp = seq[0]
        higher = qsort([i for i in seq if i >tmp])
        lower = qsort([i for i in seq if i < tmp])
        return lower + [tmp] + higher


#冒泡排序，每次对两个数进行比较，然后如果不对就重新排序
def bubblesort(seq):
    for i in range(len(seq)-1):
        for j in range(len(seq)-1-i):
            if seq[j] < seq[j+1]:
                seq[j], seq[j+1] = seq[j+1], seq[j]
    return seq
if __name__ == '__main__':
    print(bubblesort([10, 2, 4, 8, 80, 9]))