# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(0)
        dummy = temp
        carry = 0
        while l1 or l2 or carry!=0:
            s = 0
            if l1 and l2:
                s = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            elif l1:
                s = l1.val + carry
                l1 = l1.next
            elif l2:
                s = l2.val + carry
                l2 = l2.next
            else:
                s = carry
            n = s%10
            carry = s//10
            dummy.next = ListNode(n)

            dummy = dummy.next
        return temp.next

