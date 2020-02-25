from generic_heap import Heap as GenericHeap
class Heap(GenericHeap):
  def __init__(self):
    super().__init__(lambda v1, v2: v1 > v2)

  def get_max(self):
    pass