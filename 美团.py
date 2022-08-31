# # n, m = map(int, input().split())
# # S = input()
# # s = input()

# # def solution(S, s, n, m):
# #     print(S, s, n, m)

# #     def match(origin, new):
# #         res = True
# #         for i in range(len(origin)):
# #             if origin[i] != new[i] and new[i] != '*':
# #                 res = False
# #                 break
# #         return res
# #     ans = 0
# #     for i in range(n - m + 1):
# #         if match(S[i:i+m], s):
# #             ans += 1
# #     return ans

# # if __name__ == '__main__':
# #     # print(solution(S, s, n, m))
# #     print(solution('abcaacc', 'a*c', 7, 3))

# # n = int(input())
# # m = int(input())
# # S = input()
# # X = list(map(int, input().split(' ')))
# # strs = []
# # m = t
# # while m:
# #     m -= 1
# #     strs.append(input())
# # res = 0
# # visited = [False] * len(strs)

# # def dfs(path):
# #     global res
# #     if len(path) == len(S):
# #         if path == S and visited == [True]*len(strs):
# #             res += 1
# #         return
# #     for i in range(len(strs)):
# #         if not visited[i]:
# #             visited[i] = True
# #             dfs(path + strs[i])
# #             visited[i] = False

# # dfs('')
# # print(res)

# # n, m = list(map(int, input().split(' ')))
# # S = input()
# # X = list(map(int, input().split(' ')))
# # # n = 6
# # # m = 2
# # # S = 'aaaaa'
# # # X = ['aaaa', 'aa']
# # strs = []
# # while m:
# #     m -= 1
# #     strs.append(input())
# # res = 0
# # visited = [False] * len(strs)

# # print(strs, visited)

# # def dfs(path):
# #     global res
# #     if len(path) == len(S):
# #         if path == S and visited == [True]*len(strs):
# #             res += 1
# #         return
# #     for i in range(len(strs)):
# #         if not visited[i]:
# #             visited[i] = True
# #             dfs(path + strs[i])
# #             visited[i] = False

# # visited = [False] * len(strs)
# # if n == sum(X):
# #     dfs('')
# # print(res)

# # n, m = list(map(int, input().split(' ')))
# # S = input()
# # X = list(map(int, input().split(' ')))
# # strs = []
# # while m:
# #     m -= 1
# #     strs.append(input())
# # strs.sort()
# # res = 0
# # visited = [False] * len(strs)

# # def dfs(path):
# #     global res
# #     if len(path) == len(S):
# #         if path == S and visited == [True]*len(strs):
# #             res += 1
# #         return
# #     p = len(path)
# #     if path != S[:p]:
# #         return
# #     for i in range(len(strs)):
# #         if i >= 1 and strs[i] == strs[i-1] and not visited[i-1]:
# #             continue
# #         if not visited[i]:
# #             visited[i] = True
# #             dfs(path + strs[i])
# #             visited[i] = False

# # visited = [False] * len(strs)
# # if n == sum(X):
# #     dfs('')
# # print(res)

# # n, m = map(int, input().split())
# # S = input()
# # input()
# # s = list()
# # piece = list()
# # while True:
# #     try:
# #         piece.append(input())
# #     except:
# #         break

# # 徐天一  17: 53: 21
# n, m = map(int, input().split())
# S = input()
# num = len(list(map(int, input().split())))
# s = list()
# for _ in range(num):
#     s.append(input())

# def solution(S, s, m):
#     visit = [True for _ in range(m)]
#     temp = ["" for _ in range(m)]
#     res = set()

#     def dfs(position):
#         if position == len(s):
#             res.add(tuple(temp))
#             return

#         for i in range(m):
#             if visit[i]:
#                 temp[position] = s[i]
#                 visit[i] = False
#                 dfs(position+1)
#                 visit[i] = True

#     dfs(0)

#     ans = 0
#     for i in res:
#         if "".join(list(i)) == S:
#             ans += 1
#     return ans

# # s = ['aaaa', 'aa']
# # S = 'aaaaaa'
# if __name__ == '__main__':
#     print(solution(S, s, m))

#


def subArr(originArray):
    result = []
    size = len(originArray)
    for i in range(size):
        for j in range(i, size):
            if i == j:
                result.append([originArray[i]])
            else:
                result.append(originArray[i:j + 1])
    return result


def goodNum(k, num):
    res = 0
    listNum = subArr(num)
    for item in listNum:
        item.sort()
        if len(item) > 0 and item[-1] == k * item[0]:
            res += 1
    return res


if __name__ == '__main__':
    n, k = 4, 2
    num = [4, 2, 3, 7]
    print(goodNum(n, k, num))

if __name__ == '__main__':
    n, k = map(int, input().split())
    num = list(map(int, input().split()))
    print(goodNum(k, num))

# def subArr(originArray):
#     result = []
#     size = len(originArray)
#     for i in range(size):
#         for j in range(i, size):
#             if i == j:
#                 result.append([originArray[i]])
#             else:
#                 result.append(originArray[i:j + 1])

#     return result

# print(subArr([4, 3, 2, 7]))
