# This Python file uses the following encoding: utf-8
from collections import Counter
a = ['a', 'a', 'b', 'c', 2, 3, 32, 2, 2]
c = Counter(a)
# c = Counter(a).most_common()
# c.update('aaasccs')
c.subtract('aabc')
print(c)