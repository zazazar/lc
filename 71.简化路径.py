#
# @lc app=leetcode.cn id=71 lang=python3
#
# [71] 简化路径
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        newpath = []

        for item in path:
            # 所有字母
            if item != "" and item != "." and item != "..":
                newpath.append(item)
            # 所有..
            elif item == "..":
                if len(newpath) >= 1:
                    newpath.pop()

        result = ""
        if len(newpath) == 0:
            print("/")
            return "/"
        else:
            for x in newpath:
                result = result + '/'
                result = result + str(x)

        print(result)

        return result


# @lc code=end
if __name__ == "__main__":
    Solution().simplifyPath("/a/./b/../../c/")

