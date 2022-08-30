#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 最终的返回值是深度，那么终止条件里返回的也应该是深度

#


class Solution:
    def minDepth(self, root: TreeNode):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        # 左子树和右子树的深度用递归
        # 后序遍历
        leftMinDepth = self.minDepth(root.left)
        rightMinDepth = self.minDepth(root.right)

        if root.left and not root.right:
            return leftMinDepth + 1
        if not root.left and root.right:
            return rightMinDepth + 1

        return min(leftMinDepth, rightMinDepth) + 1

    # @lc code=end


if __name__ == "__main__":
    a = TreeNode(3)
    b = TreeNode(9)
    c = TreeNode(20)
    d = TreeNode(15)
    e = TreeNode(7)
    f = TreeNode(6)

    a.left = b
    a.right = c
    c.left = d
    c.right = e
    e.left = f

    print(Solution().minDepth(a))
