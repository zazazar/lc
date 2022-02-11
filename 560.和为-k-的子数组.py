#
# @lc app=leetcode.cn id=560 lang=python3
#
#

# @lc code=start
class Solution:
    def subarraySum1(self, nums, k):
        presum = [0]
        cur = 0
        res = 0
        for item in nums:
            presum.append(item+presum[-1])
        print(presum)
        for i in range(len(presum)):
            for j in range(i+1, len(presum)):
                cur = presum[j]-presum[i]
                if cur == k:
                    res += 1
        return res

    def subarraySum(self, nums, k):
        count = 0
        mp = {0:1}
        cursum = 0
        find = 0

        for item in nums:
            cursum += item
            find = cursum - k
            if find in mp:
                count += mp[find]
            if cursum in mp:
                mp[cursum] += 1
            else:
                mp[cursum] = 1
        
        return count
            

# @lc code=end
print(Solution().subarraySum([-1,-1,1], 1))

