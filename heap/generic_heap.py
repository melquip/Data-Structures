class Heap:
  def __init__(self):
    self.size = -1
    self.storage = []

  """
  Arr[(i-1)/2] Returns the parent node.
  Arr[(2*i)+1] Returns the left child node.
  Arr[(2*i)+2] Returns the right child node.
  """
  def comparator(self, v1, v2):
    return v1 > v2
  def _swap(self, i1, i2):
    self.storage[i1], self.storage[i2] = self.storage[i2], self.storage[i1]
  def _parent(self, index):
    if index == 0: return 0
    return (index - 1) // 2
  def _parentOf(self, index):
    return self.storage[self._parent(index)]
  def _left(self, index):
    return (2 * index) + 1
  def _right(self, index):
    return (2 * index) + 2
  def _leftOf(self, index):
    return self.storage[self._left(index)]
  def _rightOf(self, index):
    return self.storage[self._right(index)]
  def _isLeaf(self, index): 
    if index >= (self.size // 2) and index <= self.size: 
      return True
    return False

  def insert(self, value):
    self.size += 1
    self.storage.insert(self.size, value)
    print(f'insert {value} at {self.size}, {self.storage}')
    self._bubble_up(self.size - 1)

  def delete(self):
    if self.size == -1:
      raise IndexError("Can't pop from empty heap")
    root = self.storage[0]
    if self.size > 0:  # more than one element in the heap
      self.storage[0] = self.storage[self.size]
      self._sift_down(0)
    self.size -= 1
    return root

  def get_priority(self):
    pass

  def get_size(self):
    return self.size

  """
  Moves the element at the specified index "up" the heap by swapping it with its parent if the parent's value is less than the value at the specified index.
  """
  def _bubble_up(self, index):
    current = self.storage[index]
    parent_index = self._parent(index)
    parent_value = self._parentOf(index)
    if index > 0 and self.comparator(current, parent_value):
      self._swap(parent_index, index)
      self._bubble_up(parent_index)
    return
  """
  Grabs the indices of this element's children and determines which child has a larger value. If the larger child's value is larger than the parent's value, the child element is swapped with the parent.
  """
  def _sift_down(self, index):
    # If the node is a non-leaf node 
    if not self._isLeaf(index): 
      # and smaller than any of its child
      if (self.storage[index] < self._leftOf(index) or self.storage[index] < self._rightOf(index)): 
        # Swap with the left child and continue with the left child 
        if self.comparator(self._leftOf(index), self._rightOf(index)): 
          self._swap(index, self._left(index)) 
          self._sift_down(self._left(index)) 
        else: 
          # Swap with the right child and continue with the right child 
          self._swap(index, self._right(index)) 
          self._sift_down(self._right(index)) 

"""
heap = Heap()
heap.insert(6)
heap.insert(8)
heap.insert(10)
heap.insert(9)
heap.insert(1)
heap.insert(9)
heap.insert(9)
heap.insert(5) 

# [10, 9, 9, 6, 1, 8, 9, 5]
for i in range(0, (heap.size//2 - 1)): 
  print("-> PARENT : " + str(heap.storage[i]) + 
  " | LEFT CHILD : " + str(heap.storage[(2 * i) + 1]) + 
  " | RIGHT CHILD : " + str(heap.storage[(2 * i) + 2])
  )
print(heap.storage)
"""