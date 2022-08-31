#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.curSum = 0
        self.res = False

    def calSum(self, root: TreeNode, targetSum: int):

        self.curSum += root.val

        if not root.left and not root.right:
            if self.curSum == targetSum:
                self.res = True
            return
        if root.left:
            self.calSum(root.left, targetSum)
            self.curSum -= root.left.val
        if root.right:
            self.calSum(root.right, targetSum)
            self.curSum -= root.right.val

        return

    def hasPathSum(self, root: TreeNode, targetSum: int):
        if not root:
            return False
        self.calSum(root, targetSum)
        return self.res


# @lc code=end

if __name__ == "__main__":
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    f = TreeNode(6)
    g = TreeNode(7)

    a.left = b
    a.right = c
    c.left = d
    c.right = e
    e.left = f

    # a.left = b
    # a.right = c
    # b.left = d
    # b.right = e
    # c.left = f
    # c.right = g

    print(Solution().hasPathSum(a, 15))
