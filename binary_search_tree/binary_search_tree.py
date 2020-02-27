import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if not self.value:
            self = BinarySearchTree(value)
        if value >= self.value:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else: 
                self.right.insert(value)
        else:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if not self.value:
            return False
        if target == self.value:
            return True
        elif target > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
        else:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if not self.value:
            return 0
        max = self.value

        # Without recursion
        # current = self
        # while current.right is not None:
        #     if current.right.value > max:
        #         max = current.right.value
        #     current = current.right
        # return max

        # With recursion
        if self.right:
            return self.right.get_max()
        return max

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):

        # current = self
        # while current.right is not None and current.left is not None:
        #     cb(current.value)
        #     cb(current.right.value)
        #     cb(current.left.value)
        #     current = current.right

        if not self.value:
            return  
        else:
            cb(self.value)
            if self.right:
                self.right.for_each(cb)
            if self.left:
                self.left.for_each(cb)
        

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

# tree = BinarySearchTree(5)
# tree.insert(2)
# tree.insert(3)
# tree.insert(7)
# print('The result of contains', tree.contains(7))