# This Python file uses the following encoding: utf-8
#快速重排，任选一个，那就第一个吧，然后选出比它大的，继续重排，小的继续重排

def qsort(seq):
    if seq == []:
        return []
    else:
        tmp = seq[0]
        higher = qsort([i for i in seq if i > tmp])
        lower = qsort([i for i in seq if i < tmp])
        return lower + [tmp] + higher
#(nlgn)

#冒泡排序，每次对两个数进行比较，然后如果不对就重新排序
def bubblesort(seq):
    for i in range(len(seq)-1):
        for j in range(len(seq)-1-i):
            if seq[j] < seq[j+1]:
                seq[j], seq[j+1] = seq[j+1], seq[j]
    return seq

#选择排序，每一次排序选择出一个最小的
def choose_sort(seq):
    for i in range(len(seq)-1):
        min_index = i
        for j in range(i+1, len(seq)):
            if seq[j] < seq[min_index]:
                min_index = j           #不要和冒泡算法搞混掉了
        seq[i], seq[min_index] = seq[min_index], seq[i]

    return seq

#插入排序，将待排列数据按照大小插入到已排序队列中
def insert_sort(seq):
    pass


#list reverse
list = ['i', 'love', 'you', 'and', 'you', 'love', 'me']
def list_reverse(list):
    for i in range(len(list)//2):
        list[i], list[len(list)-i-1] = list[len(list)-i-1], list[i]
    print(list)


#归并排序，将数组分成两个，然后进行不断的有序合并
def merge(a, b, tmp=None): #这里注意不要直接用[]
    if tmp == None:
        tmp = []
    if len(a) <= 0 or len(b) <= 0:
        tmp.extend(a)
        tmp.extend(b)
        return tmp
    if a[0] > b[0]:
        tmp.append(b[0])
        del b[0]
    else:
        tmp.append(a[0])
        del a[0]
    return merge(a, b, tmp)

def merge_sort(seq):
    if len(seq) <= 1:
        return seq
    middle = len(seq)//2
    left = merge_sort(seq[:middle])
    right = merge_sort(seq[middle:])
    return merge(left, right)


if __name__ == '__main__':
    # print(bubblesort([10, 2, 4, 8, 80, 9]))
    print(merge_sort([10, 2, 3, 4, 80, 9, 70, 50, 71]))
