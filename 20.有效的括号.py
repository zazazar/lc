#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        curarr = list(s)
        checkarr = []
        checkarr.append(0)

        result = True

        for index,simbol in enumerate(curarr):
            if simbol == '{' or simbol == '[' or simbol == '(':
                checkarr.append(simbol)
            else:
                comparesimbol = checkarr[-1]
                checkarr.pop()
                if (simbol=='}' and comparesimbol=='{') or (simbol==']' and comparesimbol=='[') or (simbol==')' and comparesimbol=='('):
                    result = True
                else:
                    result = False
                    break

        if len(checkarr)!= 1:
            result = False
        
        print(result)
        return result

# @lc code=end
if __name__ == "__main__":
    sol = Solution().isValid('[[[)')

