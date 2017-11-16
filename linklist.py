# This Python file uses the following encoding: utf-8
#链表的节点，节点的第一个位置存值，第二个位置存放下一个节点的信息
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return '<Node val:%s next:%s>' %(self.val, self.next)
    __repr__ = __str__

class LinkList():
    '''
       head:头节点，只保存下个节点的信息
       length:初始化长度为0
       '''
    def __init__(self):
        self.head = Node(None)
        self.length = 0

    def __len__(self):
        return self.length

    # 判断是否是一个空链表
    def is_empty(self):
        return self.length == 0

    def append(self, node):
        '''
        :param node:
        :return:在链表末尾加上数据
        如果是一个空的链表，那么就让头节点指向新增加的节点
        '''
        item = None
        if isinstance(node, Node):
            item = node
        else:
            item = Node(node)

        if self.is_empty():
            self.head.next = item
        else:
            current = self.head
            while current.next != None:   #判断节点的next，也就否是尾节点是否为空
                current = current.next
            current.next = item
        self.length += 1

    #在末尾插入一串数组
    def initlist(self, list_data):
        if not isinstance(list_data, list):
            raise TypeError(u'插入对象错误')
        for i in list_data:
            self.append(i)

    #检索某个元素是否在链表里面
    def search(self, item):
        current = self.head
        found_itme = False
        while current.val !=item and current.next!=None:
            current = current.next
        if current.val == item:
            found_itme = True
        return found_itme

    #给出索引的位置
    def find(self, item):
        if not self.search(item):
            raise ValueError(u'%s不在此链表中' % item)
        count = 0
        current = self.head.next
        while current.val != item:
            current = current.next
            count += 1
        return count
    #去掉首个要去掉的元素
    def remove(self, item):
        if not self.search(item):
            raise ValueError(u'%s不在此链表中' % item)
        pre = self.head
        current = self.head.next
        while current.val != item:
            pre = pre.next
            current = current.next
        pre.next = current.next
    #
    def insert(self, pos, item):
        if pos < 0 or pos >self.length:
            raise ValueError(u'无效的位置%s' % pos)
        if not isinstance(item, Node):
            item = Node(item)
        count = 0
        current = self.head.next
        while count != pos:
            count += 1
            current = current.next
        trans = current.next
        current.next = item
        item.next = trans

    #链表的成对调换
    '''
    1->2->3->4   to  2->1->4->3
    '''
#思路，每次先将要交换的值保存起来，然后将头部指向n2,
# n1 is pointed to None or head(new).next
#if the head is None means that the length may be odd,
# and if the head.next is None that is the end
#return the head(new)


def swapPairs(head):
    if head.next != None and head!=None:
        n1 = head.next
        n2 = head.next.next
        head.next = n2
        n1.next = swapPairs(n2).next or None
        n2.next = n1
    return head


# def swapPairs(head):
#     if head != None and head.next != None:
#         next = head.next
#         head.next = swapPairs(next.next)
#         next.next = head
#         return next
#     return head

if __name__ == '__main__':

    # a = LinkList()
    # a.append(3)
    # a.initlist([1, 2, 3])
    # a.append(5)
    # a.insert(1, 4)
    # a.insert(2, 'ab')
    b = LinkList()
    b.initlist([1, 2,3,4,5,6,7,8])
    print(swapPairs(b.head))


    # list1 = Node(1, Node(2, Node(4))) #常见的无头节点的单向链表
    # print(list1.next)