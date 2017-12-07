# This Python file uses the following encoding: utf-8
#cahrrupaixud
def insert_list(list):
    for i in range(1, len(list)):
        j = i - 1
        key = list[i]
        while j >= 0:
            if list[j] > key:
                list[j + 1] = list[j]
                list[j] = key
            j -= 1
    return (list)

#fuzadun**2
# print(insert_list([1, 3, 2, 5]))

#suoyoujiange wei d de zuhe
def get_d_list(list, d, tmp=None):
    if tmp == None:
        tmp = []
    if len(list) <= d:
        return tmp
    elem1 = list[0]
    elem2 = list[d]
    list.pop(0)
    tmp.append((elem1, elem2))
    return get_d_list(list, d, tmp)
# print(get_d_list([1,2,3,4,5],2))


def check_string(string, circle_str=False):
    str_list = list(string)
    if len(str_list) < 2:
        return circle_str
    index1 = str_list.pop(0)
    index2 = str_list.pop(-1)
    if not index1 == index2:
        return False
    circle_str = True
    return check_string(''.join(str_list), circle_str)

