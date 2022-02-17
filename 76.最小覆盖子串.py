#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
import copy
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        cnt = len(t)
        curarr = []
        resarr = []
        for item in t:
            if item not in need:
                need[item] = 1
            else:
                need[item] += 1
        l,r = 0,0
        # 右边
        while r < len(s):
            if s[r] in need:
                need[s[r]] -= 1
                curarr.append(s[r])
            else:
                need[s[r]] = -1
                curarr.append(s[r])
            if need[s[r]] >= 0:
            # if s[r] in t and :
                cnt -= 1
            # 左边
            if cnt <= 0:
                while l <= r:
                    if need[s[l]] + 1 > 0:
                        break
                    else:
                        need[s[l]] += 1
                        curarr.pop(0)
                        l += 1
                if resarr == []:
                    resarr = copy.deepcopy(curarr)
                elif len(curarr) < len(resarr):
                    resarr = copy.deepcopy(curarr)
            r += 1 

        return ''.join(resarr)
# @lc code=end

