class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.capacity = capacity
        self.c = 0
        self.left.next = self.right
        self.right.prev = self.left
        self.dic = {}

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node):
        self.right.prev.next = node
        node.prev = self.right.prev
        self.right.prev = node
        node.next = self.right

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        self.remove(self.dic[key])
        self.insert(self.dic[key])
        return self.dic[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic[key].val = value
            self.remove(self.dic[key])
            self.insert(self.dic[key])
        else:
            node = Node(key,value)
            self.dic[key] = node
            if self.c == self.capacity:
                del(self.dic[self.left.next.key])
                self.remove(self.left.next)
                self.c-=1
            self.insert(self.dic[key])
            self.c+=1
        






        