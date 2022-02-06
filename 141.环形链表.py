#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
from sys import dont_write_bytecode


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         pos = set()
#         while head:
#             if head in pos:
#                 return True
#             pos.add(head)
#             head = head.next
#         return False

class Solution:
    def hasCycle(head) -> bool:
        if not head or not head.next:
            return False

        slow = head
        fast = head.next

        while slow != fast:
            if not slow.next or not fast.next.next:
                return False
            slow = slow.next
            fast = fast.next.next
        
        return True
        
# @lc code=end
if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)

    a.next = b
    b.next = c
    # c.next = a
    # print(Solution.hasCycle(a))
    if not b.next.next:
        print(1)
    else:
        print(0)