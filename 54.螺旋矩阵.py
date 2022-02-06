#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#
from typing import List
import math

# @lc code=start


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, left = 0, 0
        startbottom, startright = len(matrix)-1, len(matrix[0])-1
        bottom, right = len(matrix)-1, len(matrix[0])-1
        cycle = math.ceil(min(bottom+1, right+1)/2)
        finalarraay = []

        for i in range(cycle):

            # 上
            for x in range(left, right):
                if len(finalarraay) == len(matrix)*len(matrix[0]):
                    return finalarraay
                finalarraay.append(matrix[top][x])
            # 右
            for y in range(top, bottom):
                if len(finalarraay) == len(matrix)*len(matrix[0]):
                    return finalarraay
                finalarraay.append(matrix[y][right])
            # 下
            rightindex = right
            for z in range(left+1, right+1):
                if len(finalarraay) == len(matrix)*len(matrix[0]):
                    return finalarraay
                finalarraay.append(matrix[bottom][rightindex])
                rightindex -= 1
            # 左
            bottomindex = bottom
            for q in range(top+1, bottom+1):
                if len(finalarraay) == len(matrix)*len(matrix[0]):
                    return finalarraay
                finalarraay.append(matrix[bottomindex][left])
                bottomindex -= 1

            top += 1
            bottom -= 1
            left += 1
            right -= 1

        if startright == startbottom and (startright % 2) == 0:
            tt = int(startright/2)
            num = matrix[tt][tt]
            finalarraay.append(num)

        return finalarraay

# @lc code=end


if __name__ == '__main__':
    sol = Solution()
    x = sol.spiralOrder([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [
        11, 12, 13, 14, 15], [16, 17, 18, 19, 20]])
    y = sol.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    z = sol.spiralOrder(
        [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])
    q = sol.spiralOrder(
        [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]])
    p = sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])
    c = sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
    print(x)
