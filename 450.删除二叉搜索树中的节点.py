#
# @lc app=leetcode.cn id=450 lang=python3
#
# [450] 删除二叉搜索树中的节点
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root, key):
        if not root:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        # 找到节点
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            minNode = root.right
            while minNode.left:
                minNode = minNode.left
            root.right = self.deleteNode(root.right, minNode.val)
            minNode.left = root.left
            minNode.right = root.right
            return minNode
        return root

   
# @lc code=end
a = TreeNode(5)
b = TreeNode(2)
c = TreeNode(6)
d = TreeNode(1)
e = TreeNode(4)
f = TreeNode(7)
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
Solution().deleteNode(a, 1)

