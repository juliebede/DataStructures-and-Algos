class Node:
  
  def __init__(self, data):
    self.data = data
    self.next = None

  def get_data(self):
    return self.data


class Multiset: 

  ## Initialized state
  def __init__(self):
    self.head = None

  def __str__(self):
    full_list = ''
    current = self.head
    while (current != None):
      full_list += f'{current.get_data()} '
      current = current.next
  
    return full_list

  def add(self, item):
    if (self.head == None):
      self.head = Node(item)
    else:
      temp = self.head
      self.head = Node(item)
      self.head.next = temp


  # def delete(self, item):
  #   self.items.remove(item)

  

M = Multiset()
M.add(10)
M.add(12)
print(M)