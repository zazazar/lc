#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第K小的元素
#

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.order = 0
        self.res = 0
    def kthSmallest(self, root, k: int) -> int:

        if not root:
            return
            
        self.kthSmallest(root.left, k)

        self.order += 1
        print(root.val) 
        print(self.order)
        print(k)
        if self.order == k:
            self.res = root.val
            return self.res
        
        self.kthSmallest(root.right, k)

        return self.res
# @lc code=end
print(Solution().kthSmallest(TreeNode(2),1))
