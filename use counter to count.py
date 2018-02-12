# This Python file uses the following encoding: utf-8
# from collections import Counter
# a = ['a', 'a', 'b', 'c', 2, 3, 32, 2, 2]
# c = Counter(a)
# # c = Counter(a).most_common()
# # c.update('aaasccs')
# c.subtract('aabc')
# print(c)
# for i in {1, 2, 3}:
#     print(hash(i))
a = [1]
b = [1]
# print(hash(a[0]), hash(b[0]))
# print(set('abc'))
# print(336 >> 2)
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return '<val:%s,left:%s,right:%s>' % (self.val, self.left, self.right)
class Tree(object):
    def __init__(self):
        self.root = Node(-1)
        self.queue = []
    #cengci
    def insert(self, seq):
        while len(seq) != 0:
            node = Node(seq.pop(0))
            if self.root.val == -1:
                self.root = node
                self.queue.append(node)
            else:
                treenode = self.queue[0]
                if not treenode.left:
                    treenode.left = node
                    self.queue.append(node)
                else:
                    treenode.right = node
                    self.queue.append(node)
                    self.queue.pop(0)
    def front_search(self, root):
        if not root:
            return

        self.front_search(root.left)
        print(root.val)
        self.front_search(root.right)


    def search_root(self, root):
        if not root:
            return
        queue = []
        node = root
        queue.append(node)
        while queue:
            node = queue.pop(0)
            print(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    def deep(self,root):
        if not root:
            return 0
        return max(self.deep(root.left), self.deep(root.right)) + 1
#根据前序和中序重构
def recur_the_tree(pre,tin):
    if not pre or not tin:
        return None
    root = Node(pre[0])
    i = tin.index(root.val)
    root.left = recur_the_tree(pre[1:i+1],tin[:i])
    root.right = recur_the_tree(pre[i+1:],tin[i+1:])
    return root
#树的镜像
def mirror_the_tree(root):
    if not root:
        return None
    root.left, root.right = root.right, root.left
    mirror_the_tree(root.left)
    mirror_the_tree(root.right)
    return root

def issym_(left, right):
    if not left and not right:
        return True
    if not left or not right:
        return False
    if left.val != right.val:
        return False
    return issym_(left.left, right.right) and issym_(left.right, right.left)
def issym(root):
    return issym_(root.left, root.right)

#判断b是不是a的子结构树
def is_subtree(a, b):
    def is_tree_same(a, b):
        if a == None and b == None:
            return True
        if (a == None and b != None) or (a!=None and b == None):
            return False
        if a.val != b.val:
            return False
        return is_tree_same(a.left, b.left) and is_tree_same(a.right, b.right)
    if not b:
        return False
    if is_tree_same(a, b):
        return True
    else:
        return is_tree_same(a.left, b) or is_tree_same(a.right,b)

#1.二叉查找树
def the_lastparent(key1,key2,root):
    max_key = max(key1, key2)
    min_key = min(key1, key2)
    val = root.val
    if min_key < val < max_key:
        return val
    elif val > max_key:
        return the_lastparent(key1, key2, root.left)
    return the_lastparent(key1, key2, root.right)

#2普通的
# def the_key_stack(key1, root):
#     stack = []
#     node = root
#     stack.append(node)
#     #先遍历左节点
#     while node:
#         val = stack[-1].val
#         if val == key1:
#             return stack
#         node = node.left
#         stack.append(node)
#     node = stack[-1]
#     if node.right:



a = Tree()
a.insert([4,2,6,1,3,5,7])
# print(the_lastparent(1, 3, a.root))
# print(the_key_stack(6, a.root))
# def insert_avl(root, val):
#     if root.val == -1:
#         root = Node(val)
#     elif val < root.val:
#         r
#     else:
#         insert_avl(root.right, val)
#     return root


# def insert_seq(root,seq):
#     for i in seq:
#         root = insert_avl(root, i)
#     return root
a = Tree()
# insert_seq(a.root, [20, 10, 30])
# a.insert([1, 2, 2, 3, 4,4,3])
b = Tree()
b.insert([2,4,3])
# print(is_subtree(a.root, b.root))
# print(issym(a.root))
# print(mirror_the_tree(a.root))
# print(recur_the_tree([1, 2, 4, 5, 3, 6, 7], [4, 2, 5, 1, 6, 3, 7]))

# print(a.deep(a.root))
# a.insert([8, 9])
# print(a.queue)range(0, 10)
# a.front_search(a.root)
# a.search_root(a.root)
# print(type(range(10)))
b = 'abcd'
# for i in reversed(b):
#     print(i)
# print(b[::-1])
# from operator import itemgetter
# c = [{'x': 2, 'y':3},{'x':5,'y':6},{'x':1,'y':4}]
# c = sorted(c,key=itemgetter('x'),reverse=True)
# # print(c)
# from collections import deque
# queue= deque([1,2,3])
# queue.appendleft(4)
# print(queue)

class Node():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return '<val:%s,next:%s>'%(self.val,self.next)
a = Linklist = Node(2,Node(4,Node(5,Node(6))))
# print(a)

#1.成对交换
def Swap_pairs(linklist):
    #终止条件
    if not linklist or not linklist.next:
        return linklist
    #保存之后的链表
    node =linklist.next.next

    tmp = linklist
    linklist = linklist.next
    linklist.next = tmp
    linklist.next.next = Swap_pairs(node)
    return linklist

# print(Swap_pairs(a))
#打印最后一个
def print_last(linklist):
    curr = linklist
    while linklist.next:
        curr = linklist.next
        linklist = linklist.next
    print(curr.val)
# print_last(a)

#2.反转
def reverse_(linklist):
    if not linklist.next:
        return linklist
    curr = linklist
    b = linklist
    prev = linklist

    #获取最后一个和前一个
    while linklist.next:
        prev = linklist
        curr = linklist.next
        linklist = linklist.next

    prev.next = None
    curr.next = linklist
    linklist.next = reverse_(b)
    return linklist
def reverse_2(linklist):
    tail = None
    while linklist:
        tmp = linklist.next
        linklist.next = tail
        tail = linklist
        linklist = tmp
    return tail
# print(reverse_2(a))

#3反向打印
def print_tail_to_head(linklist):
    stack = []
    val = linklist.val
    stack.append(val)
    while linklist.next:
        linklist = linklist.next
        stack.append(linklist.val)
    return stack[::-1]
# print(print_tail_to_head(a))

#4.合并两个排序的链表
def merge(linklist1, linklist2):
    res = head = Node(0)
    while linklist1 and linklist2:
        if linklist1.val < linklist2.val:
            head.next = Node(linklist1.val)
            linklist1 = linklist1.next
        else:
            head.next = Node(linklist2.val)
            linklist2 = linklist2.next
        head = head.next
    head.next = linklist2 or linklist1
    return res.next

# print(merge(a, Node(1,Node(3,Node(4,Node(7)))) ))

#5.两个链表的第一个公共节点
# 就是前面遍历然后都放到一个栈里面

#6.删除链表的重复节点
# def cut_repeat(linklist):
#     if not linklist.next:
#         return linklist
#     curr = linklist
#     prev = Node(0)
#     while curr:
#         if curr.next and curr.val == curr.next.val:
#             curr.next = curr.next.next
#             prev = curr
#             curr = curr.next
