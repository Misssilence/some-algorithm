# This Python file uses the following encoding: utf-8
a = ((1, 3), (2, 3), (3, 4))
new_data = []
for i in a:
    new_data.append(i)
print(new_data)
print([[i for i in x] for x in a])
b = [2, 2, 3, 4, 5, 5, 6]
new_data = []
[new_data.append(i) for i in b if i not in new_data]
print(new_data)