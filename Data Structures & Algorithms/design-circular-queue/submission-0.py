class ListNode:
    def __init__(self,v):
        self.v = v
        self.next = None
        self.prev = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.count = 0
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def enQueue(self, value: int) -> bool:
        if self.count >= self.k:
            return False
        node = ListNode(value)
        self.count+=1
        temp = self.tail.prev
        self.tail.prev = node
        node.next = self.tail
        node.prev = temp
        temp.next = node
        return True

    def deQueue(self) -> bool:
        if self.count == 0:
            return False
        self.count-=1
        temp = self.head.next
        self.head.next = temp.next
        temp.next.prev = self.head
        del temp
        return True

    def Front(self) -> int:
        if self.count == 0:
            return -1
        return self.head.next.v

    def Rear(self) -> int:
        if self.count == 0:
            return -1
        return self.tail.prev.v

    def isEmpty(self) -> bool:
        if self.count == 0:
            return True
        return False

    def isFull(self) -> bool:
        if self.count == self.k:
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