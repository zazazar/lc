# 美团笔试第一题

# 神奇字符
# 题目描述
# 小美在摆弄她的字符丰。最近小团送了小美一个特殊字符*，这个字符可以和
# 其他所有字符匹配，除了这个字符外，其他字符只能自己和自己匹配。小美先前
# 有一个字符韦S，长度为n，现在她又新组合了一个可有特殊字符，*的字符串
# s，长度为m。小美想知道有多少个位置i，使得S[i+j]门与s[j]对于1≤j≤m均能匹配
# 上？其中xy代表字符串x中第y位的字符。
#
# 输入
# 7 3 // S长度7(n) s长度3(m)
# abcaacc // S
# a*c // s

# 样例输出
# 3


def magicWord(S, s, n, m):
    res = 0
    for i in range(n - m + 1):
        pivot = True
        for j in range(m):
            if s[j] != '*' and S[i + j] != s[j]:
                pivot = False
        if pivot:
            res += 1
    return res


# print(magicWord('abcaacc', 'a*c', 7, 3))

############################################################################

# 第二题

# 小团最近获得了美美团团国的裁缝资格证，成为了一个裁缝！现在小团有一个长
# 度为n的大布料S(在这个国家布料其实是一个仅包含小写英文字母的字符
# 串），小团可以将布料在任意位置剪切，例如布料abcd可以被裁剪为a与bcd 或
# ab|cd或abc与d，不过，裁剪完之后是不能拼接起来的，因为小团还不是很擅
# 长拼接布料。现在小团想知道能不能有一种裁剪方式能让他把布料恰好裁剪成客
# 人要求的小布料。
# 形式化地，有一个串S，问是否能将其划分成m个不相交的连续子串，使得这些
# 连续子串可以与要求的连续子串一一对应。（不会有多余的）

# 第一行两个空格隔开的正整数n和m，分别表示大布料S长度和客人要求的小布料数量。
# 接下来一行一个长度为n的仅包含小写英文字母的串S，表示大布料的组成。
# 接下来一行m个空格隔开的数依次表示所要求的小布料长度。
# 接下来开始m行，每行一个长度为xi的仅包含小写英文字母的串si， 表示第i个小布料的组成。
# 对于所有数据，
# 1≤m≤9,1≤n≤20,1≤xi<=n

# 样例输入：
# 6 2 // 大布料长7(n) 小布料数量为2(m)
# aaaaaa // 大布料形状(S)
# 4 2 // 每个小布料长度(piece)
# aaaa // 小布料形状(s)
# aa // 小布料形状(s)

# 输出：
# 2

# 解析：
# aaaa|aa 和 aa|aaaa 两种剪裁方式


# 思路：把小布料全排列之后拼到一起 看是否和大布料相等
class Solutions():
    # s: ['aa', 'aaaa']
    # S: 'aaaaaa'
    def cutCloth(self, S, s):

        # 全排列
        def d_dfs(nums, path, used, res, depth):
            if depth == len(nums):
                # 数组去重
                if path[:] not in res:
                    res.append(path[:])
                    return

            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    d_dfs(nums, path, used, res, depth + 1)
                    path.pop()
                    used[i] = False

            return res

        nums = s
        path = []
        used = [False for _ in range(len(nums))]
        res = []
        depth = 0
        result = d_dfs(nums, path, used, res, depth)
        print('1111', result)

        final_res = []
        for item in result:
            cur = ''.join(item)
            final_res.append(cur)
        print('3333', final_res)

        # 查看final_res里跟S重合的有几个
        ans = 0
        for item_2 in final_res:
            if S == item_2:
                ans += 1
        return ans


print(Solutions().cutCloth('aaaaaa', ['aaa', 'aaa']))

############################################################################


# 全排列解析
# nums原数组 path：cur数组 used：[False, False, False] res: 全排列的结果 depth：当前在第几层
# 走到每一层都往path数组里加一个数
def dfs(nums, path, used, res, depth):
    # 临界条件 当depth是最后一层的时候; depth只在这里起作用
    if depth == len(nums):
        # 注意是path[:]不是path
        res.append(path[:])
        return

    for i in range(len(nums)):
        # 前边所有层的数
        if not used[i]:
            # 将当前的数放到数组里
            path.append(nums[i])
            # 将当前层的used变为True
            used[i] = True
            # 遍历下一层
            dfs(nums, path, used, res, depth + 1)
            # 回溯，将当前层的used变回为False
            # 并且将path的上一层pop出来
            path.pop()
            used[i] = False

    return res


nums = [1]
path = []
used = [False for _ in range(len(nums))]
res = []
depth = 0

# print(dfs(nums, path, used, res, depth))
