class ListNode:
    def __init__(self,v):
        self.val = v
        self.next = None
        self.prev = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.k = k
        self.c = 0
        self.left.next = self.right
        self.right.prev = self.left

    def enQueue(self, value: int) -> bool:
        if self.c == self.k:
            return False
        curr = self.right.prev
        node = ListNode(value)
        curr.next = node
        node.prev = curr
        self.right.prev = node
        node.next = self.right
        self.c+=1
        return True

    def deQueue(self) -> bool:
        if self.c == 0:
            return False
        node = self.left.next.next
        node.prev = self.left
        self.left.next = node
        self.c-=1
        return True
        
    def Front(self) -> int:
        if self.c == 0:
            return -1
        return self.left.next.val


    def Rear(self) -> int:
        if self.c == 0:
            return -1
        return self.right.prev.val


    def isEmpty(self) -> bool:
        if self.c == 0:
            return True
        return False

    def isFull(self) -> bool:
        if self.c == self.k:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()