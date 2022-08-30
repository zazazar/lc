#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 层序遍历方法1
class Solution_C_1:

    def __init__(self) -> None:
        self.que = []
        self.res = []
        self.cur = []

    def levelOrder(self, root: TreeNode):
        if not root:
            return []

        self.que.append(root)
        self.res.append([root.val])

        # 层序遍历
        while len(self.que) != 0:
            temp = self.que[0]
            if temp.left:
                self.que.append(temp.left)
                self.res.append(temp.left.val)
            if temp.right:
                self.que.append(temp.right)
                self.res.append(temp.right.val)
            self.que.pop(0)

        print(self.res)


# 层序遍历方法2
class Solution_C_2:

    def levelOrder(self, root: TreeNode):
        if not root:
            return []

        que = []  # 当前层的元素 放node 不放node的value
        res = [root.val]  # 结果

        que = [root]

        while que:
            for _ in range(len(que)):
                cur = que[0]
                que.pop(0)
                if cur.left:
                    que.append(cur.left)
                    res.append(cur.left.val)
                if cur.right:
                    que.append(cur.right)
                    res.append(cur.right.val)

        return res


# while和for搭配使用输出[[1], [2, 3], [4, 5, 6, 7]]
class Solution:

    def levelOrder(self, root: TreeNode):
        if not root:
            return []

        que = []  # 当前层的元素 放node 不放node的value
        res = [[root.val]]  # 结果

        que = [root]

        while que:
            for _ in range(len(que)):
                cur = que[0]
                que.pop(0)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            xxx = list(map((lambda item: item.val), que))
            if xxx:
                res.append(xxx)

        # print(res)
        return res


class Solution2:

    def levelOrder(self, root: TreeNode):
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            num = len(queue)
            lis = []
            for _ in range(num):
                cur = queue.pop(0)
                lis.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(lis)
        return res


# @lc code=end
if __name__ == "__main__":
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    f = TreeNode(6)
    g = TreeNode(7)

    # a.left = b
    # a.right = c
    # c.left = d
    # c.right = e
    # e.left = f

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    # print(Solution().levelOrder(a))
    print(Solution_C_2().levelOrder(a))
