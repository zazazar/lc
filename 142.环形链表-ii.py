#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import List


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:

        pos = set()

        while head:
            if head in pos:
                return head
            else:
                pos.add(head)
            head = head.next
        
        return head


        
# @lc code=end
if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(2)
    a.next = b
    while a:
        a = a.next
        print(a)

    # Solution().detectCycle(a)

