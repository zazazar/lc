# 1
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


# if __name__ == '__main__':
#     n, k = map(int, input().split())
#     num = list(map(int, input().split()))
#     print(goodNum(k, num))

# if __name__ == '__main__':
#     n, k = 4, 2
#     num = [4, 2, 3, 7]
#     print(goodNum(n, k, num))

# 2