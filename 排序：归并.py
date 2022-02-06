def mergesort(nums):
    if len(nums)<=1:
        return nums

    left = mergesort(nums[:len(nums)//2])
    right = mergesort(nums[len(nums)//2:])

    return merge(left,right)

def merge(leftarr,rightarr):
    l,r = 0,0
    res = []
    for i in range(len(leftarr)+len(rightarr)):
        if leftarr[l] < rightarr[r]:
            res.append(leftarr[l])
            l += 1
        elif leftarr[l] > rightarr[r]:
            res.append(rightarr[r])
            r += 1
        else:
            res.append(leftarr[l])
            res.append(rightarr[r])
            l += 1
            r += 1
        
        if l == len(leftarr):
            res = res + rightarr[r:]
            break
        if r == len(rightarr):
            res = res + leftarr[l:]
            break
    # print(res)
    return res

print(mergesort([3,2,1]))
merge([1,4],[2,3])