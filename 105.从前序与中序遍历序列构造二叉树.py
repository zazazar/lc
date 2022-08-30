#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def buildTree(self, preorder, inorder) -> TreeNode:

        def build(preorder, preleft, preright, inorder, inleft, inright):
            if preleft > preright:
                return None
            if inleft > inright:
                return None
            root = TreeNode(preorder[preleft])
            rootvalue = preorder[preleft]
            leftsize = -1
            rightsize = -1
            for index in range(inleft, inright + 1):
                if inorder[index] == rootvalue:
                    leftsize = index - inleft
                    rightsize = inright - index
                    break

            print(root.val)

            root.left = build(preorder, preleft + 1, preleft + leftsize,
                              inorder, inleft, index - 1)
            root.right = build(preorder, preleft + leftsize + 1, preright,
                               inorder, index + 1, inright)

            return root

        return build(preorder, 0,
                     len(preorder) - 1, inorder, 0,
                     len(inorder) - 1)


# @lc code=end

Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
