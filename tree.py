# This Python file uses the following encoding: utf-8
#二叉树，二叉树的每个节点都有两个分叉，左和右
#定义节点,节点的元素为-1
class Node(object):
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild

    def __repr__(self):
        return '<elem:%s,lchild:%s,rchild:%s>' %(self.elem, self.lchild, self.rchild)

#定义树
class Tree(object):
    def __init__(self):
        self.root = Node()
        self.myq = []  #这个就是用来遍历的，每一次添加的时候会把元素加进去，如果这个节点的左右树节点都满了，就把第一个节点给去掉。
    def add(self, elem):
        node = Node(elem)
        if self.root.elem == -1:  #对根节点判断，先对根节点赋值
            self.root = node
            self.myq.append(node)
        else:
            treenode = self.myq[0]
            if not treenode.lchild:
                treenode.lchild = node
                self.myq.append(node)
            else:
                treenode.rchild = node
                self.myq.append(node)
                self.myq.pop(0) #把这个满了的树节点给扔掉
    #前序排列 根-左-右
    #前就是根在序列的前面
    def front_digui(self, root):

        if root == None:  #判断时候要注意，是判断为空，不是不存在
            return
        print(root.elem)
        self.front_digui(root.lchild)
        self.front_digui(root.rchild)

    #利用堆栈完成，堆栈堆里面分别是堆和栈，堆指的是程序在运行时被动态分配到的内存空间，程序里面就会被放在
    #栈就是利用堆的一个过程，是后进先出,堆栈实现深度优先，而队列实现的是广度优先
    def front_stack(self, root):
        if root == None:
            return
        stack = []
        node = root
        while node or stack:
            while node:   #遍历左节点
                print(node.elem)  #先打印根节点
                stack.append(node) #节点存放进去，实现后进先出
                node = node.lchild  #找到左节点
            node = stack.pop()   #把最之前最后一个节点找出来
            node = node.rchild



    #中序遍历 左-根-右
    def left_digui(self, root):
        elem = []
        if root == None:  # 判断时候要注意，是判断为空，不是不存在
            return
        self.left_digui(root.lchild)
        print(root.elem)
        elem.append(root.elem)
        self.left_digui(root.rchild)

    def left_stack(self, root):
        if root == None:
            return
        stack = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.lchild  #所有的左节点都在堆栈里面了，然后开始打印
            node = stack.pop()
            print(node.elem)
            node = node.rchild


    def right_digui(self, root):
        elem = []
        if root == None:  # 判断时候要注意，是判断为空，不是不存在
            return
        self.right_digui(root.lchild)
        self.right_digui(root.rchild)
        print(root.elem)
        elem.append(root.elem)

    def right_stack(self, root):
        if root == None:
            return
        node = root
        stack1 = []
        stack2 = []
        stack1.append(node)
        while stack1:
            node = stack1.pop()  #讲元素按照后续排列的逆序排列
            if node.lchild:
                stack1.append(node.lchild)
            if node.rchild:
                stack1.append(node.rchild)
            stack2.append(node)
        while stack2:
            print(stack2.pop().elem)



    #利用队列来完成层序遍历
    def level_ele(self, root):
        if root== None:
            return
        queue = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            print(node.elem)
            if node.lchild != None:
                queue.append(node.lchild)
            if node.rchild != None:
                queue.append(node.rchild)


a = Tree()
for i in range(0, 10):
    a.add(i)

a.right_stack(a.root)
