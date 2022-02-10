#
# @lc app=leetcode.cn id=19 lang=python3
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # 还有一个思路：要是链表不够长，可以前边添加一些节点，反正是倒着数的
    def removeNthFromEnd(self, head, n):
        a,b,h = head,head,head
        time = 0
        for i in range(n+1):
            if b == None:
                break
            b = b.next
            time += 1
        
        if b == None and time==n:
            return a.next
        if b == None and n - time == 1:
            return a.next.next

        while b:
            a = a.next
            b = b.next
        a.next = a.next.next

        return h
    
    # 虚拟节点
    def removeNthFromEnd2(self, head, n):
        dummy = ListNode(-1)
        dummy.next = head

# @lc code=end

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
a.next = b
b.next = c
c.next = d

for i in range(4):
    a = a.next
print(a)


