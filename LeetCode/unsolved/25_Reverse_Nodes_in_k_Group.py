# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


#Solve by recursion
class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        count = 0
        head_copy = head
        new_head = ListNode(0)
        new_head.next = head
        output, next_head, flag = self.helper(head, count, k)
        head_copy.next = next_head
        while (flag):
            count = 0
            output_temp, next_head, flag = self.helper(next_head, count, k)
            head_copy.next = next_head

        return output

    def helper(self, head, count, k):
        count += 1
        if head.next and count < k:
            output, next_head, flag = self.helper(head.next, count, k)
            head.next.next = head
            if head.next.next == head:
                head.next = None
            return output, next_head, flag
        else:
            print("count", count)
            if head.next:
                return head, head.next, True
            else:
                return head, head.next, False
