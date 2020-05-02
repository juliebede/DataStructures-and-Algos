class BinaryHeap:

  def __init__(self):
    self.heap = [0]
    self.size = 0
  
  def __str__(self):
    r = ""
    for val in self.heap:
      r += "{} ".format(val)
    
    return r

  def percUp(self, i):
    while (i // 2 > 0):
      if (self.heap[i] < self.heap[i // 2]):
        tmp = self.heap[i]
        self.heap[i] = self.heap[i // 2]
        self.heap[i // 2] = tmp
      
      i //= 2

  def insert(self, item):
    self.heap.append(item)
    self.size += 1
    self.percUp(self.size) # index of the last element
  
  def percDown(self):
    i = 1
    while (i * 2 <= self.size):
      minChild = i * 2
      if (minChild + 1 <= self.size and self.heap[minChild] > self.heap[minChild + 1]):
        minChild += 1
      
      if (self.heap[i] > self.heap[minChild]):
        tmp = self.heap[i]
        self.heap[i] = self.heap[minChild]
        self.heap[minChild] = tmp
      
      i = minChild
  
  def getMin(self):
    val = self.heap[1]
    self.heap[1] = self.heap[self.size]
    self.size -= 1
    self.heap.pop()


new = BinaryHeap()
new.insert(5)
new.insert(4)
new.insert(1)
print(new)
print(new.getMin())
print(new)