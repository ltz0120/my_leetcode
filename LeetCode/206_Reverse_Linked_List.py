# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        out = self.helper(head)
        return out

    def helper(self, head):
        print(head.val)
        if head.next:
            output = self.helper(head.next)
            head.next.next = head
            if head.next.next == head:
                head.next = None
            return output
        else:
            return head

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