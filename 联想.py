# def Solution(n, m, str):
#     if n >= m:
#         res = ['A' for i in range(len(str))]
#         return ''.join(res)

# def solutions(s, n, m):
#     i = 0
#     res = ''
#     while i < n and m > 0:
#         if s[i] == 'B':
#             m -= 1
#         res += 'A'
#         i += 1
#     return res + s[i:]

# print(solutions('ABBAB', 5, 2))


def solutions(m, n, x, y):
    res = 0
    minStep = min(x, y, m - x + 1, n - y + 1)
    for i in range(min(x + minStep, m)):
        for j in range(min(y + minStep, n)):
            step = abs(i - x + 1) + abs(j - y + 1)
            if step == minStep:
                res += 1
    return res


print(solutions(5, 7, 3, 3))

# from collections import defaultdict

# def solutions(m, n, x, y):
#     cnt = defaultdict(int)
#     for i in range(m):
#         for j in range(n):
#             distance = abs(x - 1 - i) + abs(y - 1 - j)
#             cnt[distance] += 1
#     armor = 0
#     return max(cnt.values())
