from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.storage = dict()
        self.order = DoublyLinkedList()
        

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.storage:
            node = self.storage[key]
            self.order.move_to_end(node)
            return node.value[1]
        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        #  Check and see if the key is in the dict
        if key in self.storage:
            # If it is
            node = self.storage[key]
            # Overwrite the value
            node.value = (key, value)
            # Move it to the end. It is upto us to decide if the head or tail is considered the most recently used.
            # In this case we are considering the tail to be most recently used.
            self.order.move_to_end(node)
            return 

        # If it isn't
        # Check and see if cache is full
        # If cache is full
        if self.size == self.limit:
            # Remove oldest entry from dict i.e the head 
            del self.storage[self.order.head.value[0]]
            # Remove oldest entry from DLL
            self.order.remove_from_head()
            # Reduce the size
            self.size -= 1
        
        # If the cache is empty:
        # Add to the linked list(key and the value)
        self.order.add_to_tail((key, value))
        # Add the key and value to the dictionary
        self.storage[key] = self.order.tail
        # Increment size
        self.size += 1


# lru = LRUCache(3)
# lru.set('item1', 'a')
# print(lru.storage)
# print(lru.order.head.value)
# print(lru.order.head.next)
# print(lru.order.head.prev)

