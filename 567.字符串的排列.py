#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        dic1 = dict()
        dic2 = dict()
        
        for item in s1:
            if item not in dic1:
                dic1[item] = 1
            else:
                dic1[item] += 1
        
        i = 0
        j = len(s1) - 1

        for item in s2[i:j+1]:
            if item not in dic2:
                dic2[item] = 1
            else:
                dic2[item] += 1

        while j < len(s2):
            if dic2 == dic1:
                return True
            else:
                dic2[s2[i]] -= 1
                if dic2[s2[i]] == 0:
                    del dic2[s2[i]]
                i += 1
                j += 1
                if j >= len(s2):
                    return False
                if s2[j] not in dic2:
                    dic2[s2[j]] = 1
                else:
                    dic2[s2[j]] += 1
        
        return False
# @lc code=end

