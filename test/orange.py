# This Python file uses the following encoding: utf-8
from pandas.core.frame import DataFrame



def to_bad(bad_index, box):  #jianhua
    try:
        if box[bad_index[0]+1][bad_index[1]] == 1:
            box[bad_index[0]+1][bad_index[1]] = 2

        if box[bad_index[0] - 1][bad_index[1]] == 1 and bad_index[0] !=0:
            box[bad_index[0] - 1][bad_index[1]] = 2

        if box[bad_index[0]][bad_index[1]+1] == 1:
            box[bad_index[0]][bad_index[1]+1] = 2

        if box[bad_index[0]][bad_index[1]-1] == 1 and bad_index[1]!=0:
            box[bad_index[0]][bad_index[1]-1] = 2
    except:
        pass
    return box

def check_good(box):
    for row in range(0, 2):
        for col in range(len(box[row])):
            if box[row][col] == 1:
                return True
    return False

def calc_rot_time(box):
    day = 0

    while check_good(box):
        bad_index_arr = []
        for row in range(0, 2):
            for col in range(len(box[row])):
                if box[row][col] == 2:
                    bad_index = (row, col)
                    bad_index_arr.append(bad_index)
        if len(bad_index_arr) == 0:
            return -1
        day += 1

        for bad_index in bad_index_arr:
            box = to_bad(bad_index, box)
            print(box)
    return day


print(calc_rot_time([[2,1,1,1],[1,1,1,1]]))
# def wulala(grid):
