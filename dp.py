# This Python file uses the following encoding: utf-8
#coin
values = [1, 2, 5, 10, 21, 25]#coin seq
def Coinmin(values, money):
    '''
    :param values:coin
    :param money: the change
    :return:
    '''
    coinUsed = [0]*(money+1) #这个用来存储之前的情况
    for cent in range(money+1):
        minCents = cent  #暂时最小的就全是一元

        for kind in range(len(values)):
            if values[kind] <= cent:
                #递推式 就是前一个最小种类+1
                temp = coinUsed[cent-values[kind]] + 1
                if temp < minCents:
                    minCents = temp

        coinUsed[cent] = minCents

    return coinUsed

print(Coinmin(values,10))


