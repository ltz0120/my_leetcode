# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


#Solve by recursion
class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return []
        out = self.helper(head)
        return out

    def helper(self, head):
        if head.next:
            output = self.helper(head.next)
            head.next.next = head
            if head.next.next == head:
                head.next = None
            return output
        else:
            return head

# Solve by Stack iteration
class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return []

        s = []
        while head:
            s.append(head)
            head = head.next
        new_head = s.pop(-1)
        out = new_head
        print(len(s))
        while s:
            new_head.next = s.pop(-1)
            new_head = new_head.next
        new_head.next = None
        return out


if __name__ == "__main__":
    linkedlist = [1,2,3,4,5]  # expected output: [5,4,3,2,1]
    headlist=[]
    for i in range(len(linkedlist)):
        head = ListNode(linkedlist[i])
        headlist.append(head)

    for i in range(len(headlist)):
        if i <len(headlist)-1:
            headlist[i].next = headlist[i+1]

    head = headlist[0]
    solution = Solution()
    new_head = solution.reverseList(head)
    while new_head:
        print(new_head.val)
        new_head = new_head.next