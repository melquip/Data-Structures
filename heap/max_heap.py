from generic_heap import Heap as GenericHeap
class Heap(GenericHeap):
  def __init__(self):
    super().__init__(lambda v1, v2: v1 > v2)
    self.maxValue = None

  def insert(self, value):
    super().insert(value)
    if self.maxValue is None or value > self.maxValue:
      self.maxValue = value
  def delete(self):
    deleted = super().delete()
    if self.size > 0:
      self.maxValue = max(self.storage[:self.size])
    else: 
      self.maxValue = self.storage[0]
    return deleted
  def get_max(self):
    return self.maxValue 