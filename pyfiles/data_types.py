class Node:
    def __init__(self, item, next = None):
        self.item = item
        self.next = next

class LinkedList:
    def __init__(self, items = None):
        self._len = 0
        self._head = None
        self._tail = None

        if items:
            for item in items:
                self.add_last(item)

    def get_tail(self):
        if not self._tail:
            raise IndexError("Cannot get tail from empty list")
        return self._tail.item

    def get_head(self):
        if not self._head:
            raise IndexError("Cannot get head from empty list")
        return self._head.item

    def add_last(self, item):
        if self._len == 0:
            node = Node(item)
            self._head = node
            self._tail = node
        else:
            node = Node(item, None)
            self._tail.next = node
            self._tail = node
        self._len += 1

    def add_first(self, item):
        if self._len == 0:
            node = Node(item)
            self._head = node
            self._tail = node
        else:
            node = Node(item, self._head)
            self._head = node
        self._len += 1

    def remove_first(self):
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

    def remove_last(self):
        if self._len == 0:
            raise IndexError("Cannot remove from an empty list")
        
        removed = self._tail.item
        
        if self._len == 1:
            self._tail = None
            self._head = None
        else:
            current_item = self._head
            while current_item.next is not self._tail:
                current_item = current_item.next
            self._tail = current_item
            self._tail.next = None

        self._len -= 1
        return removed
        

    def __len__(self):
        return self._len

class LinkedQueue:
    def __init__(self):
        self._list = LinkedList()
        self._len = 0
    
    def enqueue(self, item):
        self._list.add_last(item)
        self._len += 1

    def dequeue(self):
        if self._len == 0:
            raise IndexError("Cannot remove from an empty queue")
        removed = self._list.remove_first()
        self._len -= 1
        return removed
        
    def peek(self):
        if self._len == 0:
            raise IndexError("Cannot peek into an empty queue")
        return self._list.get_head()
    
    def is_empty(self):
        return self._len == 0

    def __len__(self):
        return self._len