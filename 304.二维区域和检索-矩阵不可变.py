#
# @lc app=leetcode.cn id=304 lang=python3
#

# @lc code=start
import copy
class NumMatrix:

    def __init__(self, matrix):
        self.presumMatrix = self.preSum(matrix)


    def preSum(self, matrix):
        presum = [[0 for i in range(len(matrix[0])+1)] for j in range(len(matrix)+1)]

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if col == 0 and row == 0:
                    presum[1][1] = matrix[0][0]
                elif col == 0:
                    presum[row+1][col+1] = presum[row][col+1] + matrix[row][col]
                elif row == 0:
                    presum[row+1][col+1] = presum[row+1][col] + matrix[row][col]
                else:
                    presum[row+1][col+1] = presum[row+1][col] + presum[row][col+1] - presum[row][col] + matrix[row][col]
        return presum


    def sumRegion(self, row1, col1, row2, col2):
        return self.presumMatrix[row2+1][col2+1] + self.presumMatrix[row1][col1] - self.presumMatrix[row1][col2+1] - self.presumMatrix[row2+1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end
matrix = [[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]
print(NumMatrix(matrix).preSum(matrix))

