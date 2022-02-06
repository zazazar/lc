# 单链表
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
a.next = b
b.next = c

# 二叉树
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

x1 = TreeNode(1)
x2 = TreeNode(2)
x3 = TreeNode(3)
x4 = TreeNode(4)
x5 = TreeNode(5)
x6 = TreeNode(6)

x1.left = x2
x1.right = x3
x2.left = x4
x2.right = x5
x3.left = x6

# 倒叙打印单链表上所有节点的值
def printList(root:ListNode):
    if not root:
        return root
    printList(root.next)
    print(root.val)
    
# printList(a) # 3 2 1

# 前序遍历二叉树（递归）
def preOrder(root):
    if not root:
        return 
    print(root.val)
    preOrder(root.left)
    preOrder(root.right)
    
# 中序遍历二叉树（递归）
def inOrder(root):
    if not root:
        return
    inOrder(root.left)
    print(root.val)
    inOrder(root.right)

# 后序遍历二叉树（递归
def postOrder(root):
    if not root:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.val)

# 层序遍历二叉树（队列）
def levelOrder(root):
    queue = []
    queue.append(root)
    res = []
    
    while queue:
        current = queue[0]
        res.append(current.val)
        queue.pop(0) # 注意pop()的用法
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    print(res)

levelOrder(x1)