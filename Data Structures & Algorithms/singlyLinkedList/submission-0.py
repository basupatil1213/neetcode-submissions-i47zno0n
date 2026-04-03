class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.size = 0

    
    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        curr = self.head.next
        idx = 0
        while curr:
            if idx == index:
                break
            idx += 1
            curr = curr.next
        
        return curr.val
            
        

    def insertHead(self, val: int) -> None:
        temp = self.head.next
        self.head.next = Node(val, temp)
        self.size += 1
        

    def insertTail(self, val: int) -> None:
        curr = self.head
        while curr and curr.next:
            curr = curr.next
        curr.next = Node(val)
        self.size += 1
        

    def remove(self, index: int) -> bool:
        if index >= self.size:
            return False
        curr = self.head
        idx = 0
        while curr and curr.next:
            if idx == index:
                curr.next = curr.next.next
                break
            curr = curr.next
            idx += 1
        self.size -= 1
        return True

        

    def getValues(self) -> List[int]:
        values = []
        curr = self.head.next

        while curr:
            values.append(curr.val)
            curr = curr.next
        
        return values
        
