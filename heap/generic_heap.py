class Heap:
  def __init__(self, comparer = None):
    self.size = -1
    self.storage = []
    if comparer is not None:
      self.comparator = comparer
    else:
      self.comparator = lambda v1, v2: v1 > v2

  """
  Arr[(i-1)/2] Returns the parent node.
  Arr[(2*i)+1] Returns the left child node.
  Arr[(2*i)+2] Returns the right child node.
  """
  def _swap(self, i1, i2):
    self.storage[i1], self.storage[i2] = self.storage[i2], self.storage[i1]
  def _parent(self, index):
    if index == 0: return 0
    return (index - 1) // 2
  def _parentOf(self, index):
    return self.storage[self._parent(index)]
  def _left(self, index):
    value = (2 * index) + 1
    if value > self.size:
      return None
    return value
  def _right(self, index):
    value = (2 * index) + 2
    if value > self.size:
      return None
    return value
  def _leftOf(self, index):
    index = self._left(index)
    if index is not None:
      return self.storage[index]
    return None
  def _rightOf(self, index):
    index = self._right(index)
    if index is not None:
      return self.storage[index]
    return None
  def _isLeaf(self, index): 
    if index >= (self.size // 2) and index <= self.size: 
      return True
    return False

  def insert(self, value):
    self.size += 1
    self.storage.insert(self.size, value)
    self._bubble_up(self.size)

  """
  Removes and returns the 'topmost' value from the heap; this method needs to ensure that the heap property is maintained after the topmost element has been removed. 
  """
  def delete(self):
    if self.size == -1:
      raise IndexError("Can't pop from empty heap")
    print('deleting:', self.storage)
    root = self.storage[0]
    # if there is more than one element in the heap
    if self.size > 0:
      self.storage[0] = self.storage[self.size]
      self._sift_down(0)
    self.size -= 1
    print('delete:', self.storage)
    return root

  def get_priority(self):
    return self.storage[0]

  def get_size(self):
    return self.size + 1

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
    current = self.storage[index]
    leftChild_i = self._left(index)
    leftChild_v = self._leftOf(index)
    rightChild_i = self._right(index)
    rightChild_v = self._rightOf(index)

    bestChild_i, bestChild_v = (leftChild_i, leftChild_v)
    if rightChild_i is not None and self.comparator(rightChild_v, leftChild_v):
      bestChild_i, bestChild_v = (rightChild_i, rightChild_v)
    if bestChild_i is not None and self.comparator(bestChild_v, current):
      self.storage[index], self.storage[bestChild_i] = bestChild_v, current
      self._sift_down(bestChild_i)
    return
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