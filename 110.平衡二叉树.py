#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root: TreeNode):
            if not root: return 0
            left = height(root.left)
            if left == -1: return -1
            right = height(root.right)
            if right == -1: return -1

            return max(left,right)+1 if abs(left - right)<2 else -1

        return  height(root)!=-1

# 这个有问题
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root: return True
        return abs(self.depth(root.left) - self.depth(root.right)) <= 1 and  self.isBalanced(root.left) and self.isBalanced(root.right)

    def depth(self,root):
        if not root: return 0
        return max(self.depth(root.left), self.depth(root.right))+2
# @lc code=end
if __name__ == "__main__":
    a = TreeNode(3)
    b = TreeNode(9)
    c = TreeNode(20)
    d = TreeNode(15)
    e = TreeNode(7)
    a.left = b
    b.left = c
    c.left = d
    # print(Solution().isBalanced(a))

    print(Solution().depth(a))