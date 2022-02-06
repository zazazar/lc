def match(s):
    arr = []
    arr.append(-1)
    s = list(s)
    res = True
    for index, x in enumerate(s):
        if x == '(' or x =='[' or x == '{':
            arr.append(x)
        else:
            cur = arr[-1]
            arr.pop()
            if (cur=='[' and x == ']') or  (cur=='{' and x == '}') or  (cur=='(' and x == ')'):
                res = True
            else:
                res = False
                return res
    
    if len(arr)!=1:
        res = False
    return res

print(match('[[[[]'))
