# def solution(A, M):
#     ans = [0 for i in range(M+1)]
#     for i in A:
#         cur = i % M
#         print(i, cur)
#         ans[cur] += 1


#     print(max(ans))
#     return max(ans)

# # for i in A:
# #     if (i < 0):
# #         cur = M - i % M
# #         print(cur)
# #         # ans[cur] += 1
# #     else:
# #         cur = i % M
# #         print(cur)
# #         # ans[cur] += 1

# # print(max(ans))


# def solutions(a, m):
#     n = len(a)
#     visited = [False] * n
#     maxLen = 1
#     for i in range(n - 1):
#         if visited[i]:
#             continue
#         size = 1
#         for j in range(i + 1, n):
#             if abs(a[j] - a[i]) % m == 0:
#                 size += 1
#                 visited[j] = True
#         if size > maxLen:
#             maxLen = size
#     return maxLen


# solution([7, 1, 11, 8, 4, 10], 20)
# # print(solutions([-3, -2, 1, 0, 8, 7, 1], 3))
# # print(-3 % 3)

# def solution(s):
#     n = len(s)
#     window = n if n % 2 == 0 else n - 1
#     while window >= 2:
#         for i in range(n - window + 1):
#             sub = s[i:i+window]
#             alpha = set(sub)
#             flag = True
#             for j in alpha:
#                 if sub.count(j) % 2 != 0:
#                     flag = False
#                     break
#             if flag:
#                 return window
#         window -= 2
#     return 0


def solution(s):
    n = len(s)
    window = n if n % 2 == 0 else n-1
    while window >= 2:
        for i in range(n-window+1):
            Target = True
            alpha = set(s[i:i+window])
            for j in alpha:
                if s[i:i+window].count(j) % 2 != 0:
                    Target = False
                    break
            if Target:
                return window
        window -= 2
    return 0


print(solution('zuz'))
# a = 'abcd'
# print(a[0:2])
