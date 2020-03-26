class Node:

  def __init__(self, item):
    self.item = item
    self.next = None

class Stack:

  def __init__(self):
    self.head = None
  
  def __str__(self):
    linked_list = ''
    current = self.head
    while (current != None):
      linked_list += f'{current.item}'
      current = current.next
    
    return linked_list

  def is_empty(self):
    return self.head == None

  def top(self):
    if (self.head != None):
      return self.head.item
  
  def push(self, item):
    if (self.head == None):
      self.head = Node(item)
    else:
      temp = self.head
      self.head = Node(item)
      self.head.next = temp
  
  def pop(self):
    if (self.head != None):
      temp = self.head
      self.head =  self.head.next
      return temp

L = Stack()
print(L.is_empty())
L.push(20)
L.push(30)
print(L.is_empty())
print(L)
print(L.top())
L.pop()
print(L)