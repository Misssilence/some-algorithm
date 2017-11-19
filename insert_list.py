# This Python file uses the following encoding: utf-8
#列表合并
#1.尾递归法，就是递归函数放在末尾，并且不做任何操作，这样就可以优化栈耗
# def insert_list(l1, l2, tmp=[]): #有序合并
#     if len(l1) == 0 or len(l2) == 0:
#         tmp.extend(l1)
#         tmp.extend(l2)
#         return tmp
#     elif (l1[0] > l2[0]):
#         tmp.append(l2[0])
#         del l2[0]
#     else:
#         tmp.append(l1[0])
#         del l1[0]
#     return insert_list(l1, l2, tmp)
#2.循环


if __name__ == '__main__':
    print(insert_list([1, 3], [2, 4, 5, 6]))
