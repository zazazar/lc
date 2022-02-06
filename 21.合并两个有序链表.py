#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        reslist = ListNode()
        init = reslist
        while list1 or list2:
            if list1.val > list2.val:
                reslist.next = ListNode(list2.val)
                reslist = reslist.next
                list2 = list2.next
            elif list1.val < list2.val:
                reslist.next = ListNode(list1.val)
                reslist = reslist.next 
            else:
                reslist.next = ListNode(list1.val)
                reslist = reslist.next
                reslist.next = ListNode(list2.val)
                reslist = reslist.next

                list1 = list1.next
                list2 = list2.next
            
            if not list1:
                reslist.next = list2
                return init.next
            if not list2:
                reslist.next = list1
                return init.next

        return init.next
            
            

# @lc code=end
a = ListNode(1)
b = ListNode(3)
c = ListNode(4)
a.next = b
b.next = c

x = ListNode(1)
y = ListNode(2)
z = ListNode(4)
x.next = y
y.next = z

res = Solution().mergeTwoLists(a,x)
while res:
    print(res.val)
    res = res.next

