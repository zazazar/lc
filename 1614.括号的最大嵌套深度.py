#
# @lc app=leetcode.cn id=1614 lang=python3
#
# [1614] 括号的最大嵌套深度
#

# @lc code=start
class Solution:
    def maxDepth(self, s: str) -> int:
        s = list(s)
        newarr = []
        maxlen = 0
        for item in s:
            if item == '(' or item == '[' or item == '{':
                newarr.append(item)
                maxlen = max(maxlen, len(newarr))
            elif item == ')' or item == ']' or item == '}':
                newarr.pop()
        
        return maxlen


# @lc code=end
Solution().maxDepth("(1)+((2))+(((3)))")
