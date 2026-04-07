class Node:
    """
    Node class for linked list. Contains item and a link to the next node.

    Created by Justin Elak
    """
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, items: list | None = None):
        """
        Initialize a new linked list, optionally with a list of items to preload.

        Created by Justin Elak
        """
        self._len = 0
        self._head = None
        self._tail = None

        if items:
            for item in items:
                self.add_last(item)

    def get_tail(self):
        """
        Returns the tail of the linked list.

        Created by Justin Elak
        """
        if not self._tail:
            raise IndexError("Cannot get tail from empty list")
        return self._tail.data

    def get_head(self):
        """
        Returns the head of the linked list.

        Created by Justin Elak
        """
        if not self._head:
            raise IndexError("Cannot get head from empty list")
        return self._head.data

    def add_last(self, item):
        """
        Adds a new item to the end of the linked list.
        :param item: The item to add.

        Created by Justin Elak
        """
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
        """
        Adds a new item to the beginning of the linked list.
        :param item: The item to add.

        Created by Justin Elak
        """
        if self._len == 0:
            node = Node(item)
            self._head = node
            self._tail = node
        else:
            node = Node(item, self._head)
            self._head = node
        self._len += 1

    def remove_first(self):
        """
        Removes an item from the beginning of the linked list and returns the removed item.

        Created by Justin Elak
        """
        if self._len == 0:
            raise IndexError("Cannot remove from an empty list")
        
        removed = self._head.data
        
        if self._len == 1:
            self._tail = None
            self._head = None
        else:
            self._head = self._head.next
            self._head.prev = None

        self._len -= 1
        return removed

    def remove_last(self):
        """
        Removes an item from the end of the linked list and returns the removed item.

        Created by Justin Elak
        """
        if self._len == 0:
            raise IndexError("Cannot remove from an empty list")
        
        removed = self._tail.data
        
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
        """
        Returns current held value for the number of nodes in the linked list.

        Created by Justin Elak
        """
        return self._len

class LinkedQueue:
    """
    Implements a Queue using a linked list.
    """

    def __init__(self):
        """
        Create an empty Queue with a linked list backing.

        Created by Justin Elak
        """
        self._list = LinkedList()
        self._len = 0
    
    def enqueue(self, item):
        """
        Adds a new item to the end of the queue
        :param item: The item to add.

        Created by Justin Elak
        """
        self._list.add_last(item)
        self._len += 1

    def dequeue(self):
        """
        Removes and returns the first item in the queue.
        :return: The first item in the queue.

        Created by Justin Elak
        """
        if self._len == 0:
            raise ValueError("Cannot remove from an empty queue.")
        removed = self._list.remove_first()
        self._len -= 1
        return removed
        
    def peek(self):
        """
        Returns the first item from the queue. Does not remove the item.

        Created by Justin Elak
        """
        if self._len == 0:
            raise ValueError("Cannot peek into an empty queue.")
        return self._list.get_head()

    def peek_all(self) -> list:
        """
        Returns a list of all items in the queue. Does not remove any items.

        Created by Justin Elak
        """
        if len(self) == 0: return []

        list = []
        node = self._list._head
        while node:
            list.append(node.data)
            node = node.next

        return list
    
    def is_empty(self):
        """
        Is the queue empty?

        Created by Justin Elak
        """
        return self._len == 0

    def __len__(self):
        """
        Returns the calculated count of all items in the queue.

        Created by Justin Elak
        """
        return self._len