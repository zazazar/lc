#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head:
            return
        if not head.next:
            return head
        self.count = 0
        inithead = head
        prehead = None
        posthead = None
        for i in range(left-1):
            prehead = head
            head = head.next
        
        posthead = head.next
        for j in range(right - left):
            if not posthead.next:
                posthead = None
            else:
                posthead = posthead.next

        # print(head.val)
        def reverse(root, length):
            self.count += 1
            if not root.next:
                return root
            if self.count == length:
                return root
            last = reverse(root.next, length)
            root.next.next = root
            root.next = None
            return last

        result = reverse(head, right-left+1)
        if prehead:
            prehead.next = result
        for k in range(right - left):
            result = result.next
        result.next = posthead

        return inithead
 
# @lc code=end
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)

c.next = e

print(Solution().reverseBetween(c, 1, 1))
