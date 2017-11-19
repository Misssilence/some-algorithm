# This Python file uses the following encoding: utf-8
#常见的迭代取值的方法
seq = [1, 2, 3, 4, 5]
#1.
index = 0
for i in seq:
    print('index:', index, 'ele:', i)
    index += 1

#2
for i in range(len(seq)):
    print('index:', i, 'ele:', seq[i])

#3
for i, e in enumerate(seq):
    print('index:', i, 'ele:', e)

for i in reversed(seq):
    print(i)

#字典遍历操作
seq = {'1': 1, "2": 2, '3': 3}
for i, v in seq.items():
    print(i, v)