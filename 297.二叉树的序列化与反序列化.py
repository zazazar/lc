#
# @lc app=leetcode.cn id=297 lang=python3
#
# [297] 二叉树的序列化与反序列化
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    # dfs
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        
        res = []
        def encode(root):
            if not root:
                res.append('#')
                return
            
            res.append(str(root.val))
            encode(root.left)
            encode(root.right)

        encode(root)
        
        print(','.join(res))
        return ','.join(res)
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        data = data.split(',')
        self.idx = 0
        print(data)
        def decode(data):
            if data[self.idx] == '#':
                self.idx += 1
                return None
            
            root = TreeNode(int(data[self.idx]))
            self.idx += 1
            root.left = decode(data)
            root.right = decode(data)
            
            return root
        
        return decode(data)
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

# @lc code=end




