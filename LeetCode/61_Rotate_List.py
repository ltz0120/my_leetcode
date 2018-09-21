class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return []
        s = []
        while head:
            s.append(head)
            head = head.next
        k = k % len(s)
        if k == 0:
            return s[0]
        else:
            s[(len(s) - k) - 1].next = None
            s[-1].next = s[0]
            return s[len(s) - k]