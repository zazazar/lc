from typing import List


class listNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def hasCircle(self, root):
        slow = root
        fast = root.next
        
        while fast and fast.next:
            if fast == slow:
                return True
            fast = fast.next.next
            slow = slow.next

        return False

a = listNode(1)
b = listNode(2)
c = listNode(3)
d = listNode(4)
e = listNode(5)
f = listNode(6)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = c

print(Solution().hasCircle(a))
        