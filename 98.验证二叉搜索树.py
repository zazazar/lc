# encoding: utf-8
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
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
        self.sol = True

    def isValidBST(self, root):
        self.isValid(root, None, None)
        return self.sol

    def isValid(self, root, max, min):
        if not root:
            return
        if max != None and root.val >= max:
            self.sol = False
        if min != None and root.val <= min:
            self.sol = False
        
        self.isValid(root.left, root.val, min)
        self.isValid(root.right, max, root.val)
# @lc code=end


a = TreeNode(5)
b = TreeNode(4)
c = TreeNode(6)
d = TreeNode(3)
e = TreeNode(7)

a.left = b
a.right = c
c.left = d
c.right = e
print(Solution().isValidBST(a))