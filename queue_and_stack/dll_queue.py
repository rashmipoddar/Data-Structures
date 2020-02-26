import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_tail(value)

    def dequeue(self):
        if self.storage.length != 0:
            return self.storage.remove_from_head()

    def len(self):
        return self.storage.length

# The runtime complexity for removing items from an array is 0(n) while the runtime complexity for removing item from linked list is 0(1)       

# a = Queue()
# print(a.size)
# print(a.storage)
# print(a.storage.head)
# print(a.storage.tail)
# print(a.storage.length)
# print('current length of queue', a.storage.length)
# a.enqueue(4)
# print('current length of queue', a.storage.length)
# a.enqueue(6)
# print('current length of queue', a.storage.length)
# print(a.dequeue())
# print('current length of queue', a.storage.length)