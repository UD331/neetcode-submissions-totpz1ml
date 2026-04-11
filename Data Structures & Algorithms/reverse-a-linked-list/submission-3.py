# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        curr = head
        while curr:
            l.append(curr.val)
            curr = curr.next
        curr = head
        n = len(l)-1
        while curr:
            curr.val = l[n]
            n-=1
            curr = curr.next
        return head