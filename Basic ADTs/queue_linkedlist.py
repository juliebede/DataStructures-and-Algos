class Node():

  def __init__(self, item):
    self.item = item 
    self.next = None
    self.prev = None

class Queue():

  def __init__(self):
    self.head = None
    self.tail = None

  def is_empty(self):
    return self.head == None

  def __str__(self):
    full_list = ''
    current = self.head
    while (current != None):
      full_list += f'{current.item} '
      current = current.next
  
    return full_list


  def push(self, item):
    if (self.is_empty()):
      self.head = Node(item)
      self.tail = self.head
    else:
      temp = self.head
      self.head = Node(item)
      self.head.next = temp
      self.head.next.prev = self.head
  
  def pop(self):
    if (not(self.is_empty())):
      item = self.tail.item
      self.tail = self.tail.prev
      self.tail.next = None
      return item

Q = Queue()
print(Q.is_empty())
Q.push(1)
Q.push(2)
Q.push(3)
print(Q)
print(Q.pop())
print(Q)



