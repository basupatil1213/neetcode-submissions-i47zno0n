class LinkedList:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
class MyHashSet:

    def __init__(self):
        self.max_length = 100
        self.values = [None for _ in range(self.max_length)]
        

    def add(self, key: int) -> None:
        if self.contains(key):
            return
        idx = key % self.max_length
        node = LinkedList(key, self.values[idx])
        self.values[idx] = node
        

    def remove(self, key: int) -> None:
        if not self.contains(key):
            return
        idx = key % self.max_length
        node = self.values[idx]
        dummy = curr = LinkedList(-1, node)
        while curr and curr.next:
            if curr.next.val == key:
                curr.next = curr.next.next
                break
            curr = curr.next
        self.values[idx] = dummy.next
        

    def contains(self, key: int) -> bool:
        idx = key % self.max_length
        node = self.values[idx]
        while node:
            if node.val == key:
                return True
            node = node.next
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)