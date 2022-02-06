#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        restarr = []
        appendtuple = []
        sol = []
        for index,num in enumerate(nums):
            restarr[:] = nums[index+1:]
            dic = {}
            # print(restarr)
            for index2,num2 in enumerate(restarr):
                dic[num2] = index2
            for index2,num2 in enumerate(restarr):
                index3 = dic.get(0-num2-num)
                if index3!=index2 and index3!=None:
                    appendtuple = [num,num2,restarr[index3]]
                    appendtuple.sort()
                    if sol.__contains__(appendtuple)==False:
                        sol.append(appendtuple)
    
        return sol
                    
                

# @lc code=end

if __name__ =='__main__':
    sol = Solution()
    sol.threeSum([1,2,3])

    nums = [-1,0,1,2,-1,-4]
    out = 0

    dic = dict()
    result = []

    for index,i in enumerate(nums):
       dic[i] = index
    print(dic)

    for indexj,j in enumerate(nums):
        for indexk,k in enumerate(nums[indexj+1:]):
            if out-j-k in dic:
                m = out-j-k
                temp = [j,k,m]
                temp.sort()
                if temp not in result:
                    result.append(temp)
    print(result)

