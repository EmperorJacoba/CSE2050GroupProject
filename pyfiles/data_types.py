class Node:
    def __init__(self, item, prev = None, next = None):
        self.item = item
        self.prev = prev
        self.next = next

class DLinkedList:
    def __init__(self, items = None):
        self._len = 0
        self.head = None
        self._tail = None

        if items:
            for item in items:
                self.addlast(item)

    def addlast(self, item):
        if self._len == 0:
            node = Node(item)
            self._head = item
            self._tail = item
        else:
            node = Node(item,self._tail)
            self._tail.next = node
            self._tail = node
        self.len += 1

    def addfirst(self, item):
        if self._len == 0:
            node = Node(item)
            self._head = item
            self._tail = item
        else:
            node = Node(item, None, self._head)
            self._head.prev = node
            self._head = Node
        self.len += 1

    def removefirst(self):
        if self._len == 0:
            raise IndexError("Cannot remove from an empty list")
        
        removed = self._head.item
        
        if self._len == 1:
            self._tail = None
            self._head = None
        else:
            self._head = self._head.next
            self._head.prev = None

        self._len -= 1
        return removed

    def removelast(self):
        if self._len == 0:
            raise IndexError("Cannot remove from an empty list")
        
        removed = self._tail.item
        
        if self._len == 1:
            self._tail = None
            self._head = None
        else:
            self._tail = self._tail.prev
            self._tail.next = None

        self._len -= 1
        return removed
        

    def __len__(self):
        return self._len

class LinkedQueue:
    def __init__(self):
        self._list = DLinkedList()
        self._len = 0
    
    def enqueue(self, item):
        self._list.addlast(item)
        self._len += 1

    def dequeue(self):
        if self._len == 0:
            raise IndexError("Cannot remove from an empty queue")
        removed = self._list.removefirst()
        self._len -= 1
        return removed
        
    def peek(self):
        if self._len == 0:
            raise IndexError("Cannot peek into an empty qeueue")
        return self._list._head.item
    
    def is_empty(self):
        pass