#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sol = curr = ListNode()
        carry = 0
        while l1 or l2:

            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            temp = carry + x + y

            if temp >= 10:
                carry = 1
                temp -= 10
            else:
                carry = 0

            # 先给curr建一个新的节点
            curr.next = ListNode(temp)
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        # 最后一个       
        if carry == 1:
            curr.next = ListNode(1)

        return sol.next


# @lc code=end
if __name__ == "__main__":
    y = x = ListNode(2)
    x.next = ListNode(4)
    x = x.next
    x.next = ListNode(3)

    j = z = ListNode(5)
    z.next = ListNode(6)
    z = z.next
    z.next = ListNode(4)
    z = z.next

    # x.val = 2
    sol = Solution().addTwoNumbers(y,j)
    print(sol.val)
    print(sol.next.val)
    print(sol.next.next.val)
    print(type(sol))