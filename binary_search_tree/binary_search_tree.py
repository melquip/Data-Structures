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
    if value < self.value:
      if self.left is None:
        self.left = BinarySearchTree(value)
      else:
        self.left.insert(value)
    elif value >= self.value:
      if self.right is None:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)
    return value

  # Return True if the tree contains the value
  # False if it does not
  def contains(self, target):
    if target is self.value:
      return True
    elif target < self.value and self.left is not None:
      return self.left.contains(target)
    elif target > self.value and self.right is not None:
      return self.right.contains(target)
    return False

  # Return the maximum value found in the tree
  def get_max(self):
    maxVal = self.value
    rightTree = self.right
    while rightTree != None:
      if rightTree.value > maxVal:
        maxVal = rightTree.value
      rightTree = rightTree.right
    return maxVal

  # Call the function `cb` on the value of each node
  # You may use a recursive or iterative approach
  def for_each(self, cb):
    cb(self.value)
    self.left.for_each(cb) if self.left is not None else None
    self.right.for_each(cb) if self.right is not None else None

  # DAY 2 Project -----------------------

  # Print all the values in order from low to high
  # Hint: Use a recursive, depth first traversal
  def in_order_print(self, node):
    if node.left is not None:
      self.in_order_print(node.left)
    print(node.value)
    if node.right is not None:
      self.in_order_print(node.right)

  # Print the value of every node, starting with the given node,
  # in an iterative breadth first traversal
  def bft_print(self, node):
    if node is None:
      return
    q = Queue()
    q.enqueue(node)
    while q.size > 0:
      node = q.dequeue()
      print(node.value)
      if node.left is not None:
        q.enqueue(node.left)
      if node.right is not None:
        q.enqueue(node.right)

  # Print the value of every node, starting with the given node,
  # in an iterative depth first traversal
  def dft_print(self, node):
    if node is None:
      return
    s = Stack()
    s.push(node)
    while s.size > 0:
      node = s.pop()
      print(node.value)
      if node.left is not None:
        s.push(node.left)
      if node.right is not None:
        s.push(node.right)

  # STRETCH Goals -------------------------
  # Note: Research may be required

  # Print Pre-order recursive DFT
  def pre_order_dft(self, node):
    print(node.value)
    if node.left is not None:
      self.pre_order_dft(node.left)
    if node.right is not None:
      self.pre_order_dft(node.right)

  # Print Post-order recursive DFT
  def post_order_dft(self, node):
    if node.left is not None:
      self.post_order_dft(node.left)
    if node.right is not None:
      self.post_order_dft(node.right)
    print(node.value)

r"""
bst = BinarySearchTree(1)
bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

      1
     / \
        8
       / \
      5
     /   \   
    3     7
   / \   / \
  2   4 6

bst.post_order_dft(bst) 
"""