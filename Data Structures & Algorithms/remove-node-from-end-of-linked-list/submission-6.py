# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        curr = head
        while curr:
            l+=1
            curr = curr.next
        if l < n:
            return head
        goal = l-n
        c = 0
        curr = head 
        prev = None
        while curr:
            if c == goal:
                if prev:
                    prev.next = curr.next
                else: 
                    head = curr.next
                break
            c+=1
            prev = curr
            curr = curr.next
        return head

