import typing


def quicksort(nums):

    def quick(left, right):
        if left >= right:
            return nums

        pivot = nums[left]
        leftindex = left 
        rightindex = right

        while leftindex!=rightindex:
            if nums[rightindex] > pivot and leftindex < rightindex:
                rightindex -= 1
            nums[leftindex] = nums[rightindex]
            if nums[leftindex] < pivot and leftindex < rightindex:
                leftindex += 1
            nums[rightindex] = nums[leftindex]
   
        # l = r
        nums[leftindex] = pivot
        
        quick(left, leftindex-1)
        quick(leftindex+1, right)

        return nums

    quick(0,len(nums)-1)

    return nums

print(quicksort([5,1,6,7,9,2,3,4,8]))
