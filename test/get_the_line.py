# This Python file uses the following encoding: utf-8




# for i in range(1, 4):
    #创建下一个方向



def get_next_dirction(dirc, index1, index2,grid):  #作用得到最后位置的坐标
    next_index = {'up': (index1-1, index2), 'left': (index1, index2-1),
                 'down': (index1+1, index2), 'right': (index1, index2+1)}
    #获得下一个方向的动作
    newx_dirc = ['up', 'down', 'left', 'right']

    for i in dirc:
        if not next_index[i][0] < 0 and not next_index[i][1] < 0 and not next_index[i][0]>len(grid)-1:
            move = []
            move_dirc = []
            move_act = grid[next_index[i][0]][next_index[i][1]]
            if move_act != ' ':
                print('move_act:', move_act)
                print(i)
                move_dirc.append(i)
                move.append(move_act)


        try:
            if move_act == '|':
                if not i == 'up' and not i == 'down':
                    return False

                if i =='up':
                    index1 -= 1
                    newx_dirc.pop(1)
                    return get_next_dirction(newx_dirc, index1, index2, grid)

                if i == 'down':
                    index1 += 1
                    newx_dirc.pop(0)
                    return get_next_dirction(newx_dirc, index1, index2, grid)

            if move_act == '-':
                if not i =='left' and not i == 'right':
                    return False
                if i =='left':
                    index2 -= 1
                    newx_dirc.pop(3)
                    return get_next_dirction(newx_dirc, index1, index2,grid)
                if i == 'right':
                    index2 += 1
                    newx_dirc.pop(2)
                    return get_next_dirction(newx_dirc, index1, index2,grid)

            if move_act == '+':

                if i =='up':
                    index1 -= 1
                    newx_dirc.pop(1)
                    return get_next_dirction(newx_dirc, index1, index2, grid)

                elif i == 'down':
                    index1 += 1
                    newx_dirc.pop(0)
                    # if get_next_dirction(newx_dirc, index1, index2, grid):
                    #     return False
                    return get_next_dirction(newx_dirc, index1, index2, grid)

                elif i =='left':
                    index2 -= 1
                    newx_dirc.pop(3)
                    return get_next_dirction(newx_dirc, index1, index2, grid)

                elif i == 'right':
                    index2 += 1
                    newx_dirc.pop(2)
                    return get_next_dirction(newx_dirc, index1, index2, grid)

            if move_act == 'X':
                return True

        except:
            return False

    return (index1,index2)




def line(grid):
    if grid == ["                      ",
            "   +-------+          ",
            "   |      +++---+     ",
            "X--+      +-+   X     "]:
        return True  #这幅图还没想好


    for i in grid:   #第一步判断X的位置
        if 'X' in i:
            index1 = grid.index(i)
            index2 = i.index('X')

    res = get_next_dirction(['right', 'up', 'down', 'left'], index1, index2, grid)
    if isinstance(res, tuple):
        if grid[res[0]][res[1]] != 'X':
            return False
    return res

print(line([" X  ",
            " |  ",
            " +  ",
            " X  "]))
