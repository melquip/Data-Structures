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
    if value is self.value:
      return False
    elif value < self.value:
      if self.left is None:
        self.left = BinarySearchTree(value)
      else:
        self.left.insert(value)
    elif value > self.value:
      if self.right is None:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)
    return True

  # Return True if the tree contains the value
  # False if it does not
  def contains(self, target):
    if target is self.value:
      return True
    elif target < self.value:
      self.left.contains(target)
    elif target > self.value:
      self.right.contains(target)
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
