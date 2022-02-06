
class Solution:
    def isValid(self, nums):

        arr = []
        arr.append(-1)
        compareitem = ''

        for index, item in enumerate(nums):
            nums = list(nums)
            if item == '(' or item=='[' or item=='{':
                arr.append(item)
            else:
                compareitem = arr[-1]
                arr.pop()
                if (compareitem=='(' and item != ')') or (compareitem=='[' and item != ']') or (compareitem=='{' and item != '}'):
                    return False
        
        if len(arr) != 1:
            return False
                
        return True

nums = ']'
print(Solution().isValid(nums))