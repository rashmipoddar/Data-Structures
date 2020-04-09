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
        # If value is >= self.value then look right
        if value >= self.value:
            # If nothing is there insert
            if self.right is None:
                self.right = BinarySearchTree(value)
            # Else recurse right
            else: 
                self.right.insert(value)
        # If value is < self.value then look left
        else:
            # If nothing is there insert
            if self.left is None:
                self.left = BinarySearchTree(value)
            # Else recurse right
            else:
                self.left.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
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
        # With recursion(My approach)
        if not self.value:
            return 0
        max = self.value
        if self.right:
            return self.right.get_max()
        return max

        # With recursion(Another approach)
        # if not self.right:
        #     return self.value
        # else:
        #     return self.right.get_max()

        # Without recursion
        # current = self
        # while current.right is not None:
        #     if current.right.value > max:
        #         max = current.right.value
        #     current = current.right
        # return max

        

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):

        # Recursive approach
        
        cb(self.value)
        if self.right:
            self.right.for_each(cb)
        if self.left:
            self.left.for_each(cb)


        

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:
            self.in_order_print(node.left)
        print(node.value)
        if node.right:
            self.in_order_print(node.right)
        

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # initialize a queue
        q = Queue()
        # push root to queue
        q.enqueue(node)
        # while queue not empty
        while q.len() != 0:
            # pop top item out of queue into temp
            temp = q.dequeue()
            # DO THE THING!!!!!!
            print(f'{temp.value}')
            # if temp has left left put into queue
            if temp.left:
                q.enqueue(temp.left)
            # if temp has right right put into queue
            if temp.right:
                q.enqueue(temp.right)
            

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # initialize a stack
        stack = Stack()
        # push root to stack
        stack.push(node)
        # while stack not empty
        while stack.len() != 0:    
            # pop top item out of stack into temp
            temp = stack.pop()
            # DO THE THING!!!!!!
            print(f'{temp.value}')
            # if temp has right 
            if temp.right:
                # put right into stack
                stack.push(temp.right)
            # if temp has left
            if temp.left:
                # left put into stack
                stack.push(temp.left)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

tree = BinarySearchTree(1)
tree.insert(8)
tree.insert(5)
tree.insert(7)
tree.insert(6)
tree.insert(3)
tree.insert(4)
tree.insert(2)
# print('The result of contains', tree.contains(7))
# def cb(value):
    # print(f'The value is {value}')
# tree.for_each(cb)
# tree.in_order_print(tree)
# tree.bft_print(tree)
# tree.dft_print(tree)
# tree.in_order_print(tree)