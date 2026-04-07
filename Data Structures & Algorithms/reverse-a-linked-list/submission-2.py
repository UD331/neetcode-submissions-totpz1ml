# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = head
        l = []
        while (n != None):
            l.append(n.val)
            n = n.next
        l = list(reversed(l))
        n = head
        temp = n
        c = 0
        print(l)
        while (n != None):
            n.val = l[c]
            c += 1
            n = n.next
        return temp