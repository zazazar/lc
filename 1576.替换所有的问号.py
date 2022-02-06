#
# @lc app=leetcode.cn id=1576 lang=python3
#
# [1576] 替换所有的问号
#

# @lc code=start
class Solution:
    def modifyString(self, s: str) -> str:

        if s == '?':
            return 'a'
            

        for index in range(len(s)):
            if s[index] == "?":
                if index > 0 and index < len(s) - 1:
                    for x in ["a", "b", "c"]:
                        if s[index - 1] != x and s[index + 1] != x:
                            s[index] = x
                            break
                if index == 0:
                    for y in ["a", "b", "c"]:
                        if s[index + 1] != y:
                            s[index] = y
                            break
                if index == len(s)-1:
                    for z in ["a", "b", "c"]:
                        if s[index - 1] != z:
                            s[index] = z
                            break


        print("".join(str(x) for x in s))
        return "".join(str(x) for x in s)

        


# @lc code=end

if __name__ == "__main__":
    Solution().modifyString("?")

