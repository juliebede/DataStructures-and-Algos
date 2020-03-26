class Node():

  def __init__(self, item, left, right):
    self.item = item
    self.left = left
    self.right = right
  
   
  def __str__(self):
    return f'{self.item}'
  
  def get_left(self):
    return self.left

  def get_right(self):
    return self.right


class BinarySearchTree():

  def __init__(self):
    self.root = None

  def is_empty(self):
    return self.root == None
  
  def __str__(self):
    return f'{self.root.item}'

  def get_root(self):
    return self.root

  def add_leaf(self, item):
    if (self.is_empty()):
      self.root = Node(item, None, None)
    else:
      current = self.root
      added = False
      while (added == False):
        if (item > current.item):
          if (current.right == None):
            current.right = Node(item, None, None)
            added = True
          else:
            current = current.right
        else:
          if (current.left == None):
            current.left = Node(item, None, None)
            added = True
          else:
           current = current.left
          
B = BinarySearchTree()
# print(B.is_empty())
B.add_leaf(9)
print(B.is_empty())
node1 = B.get_root()
node1 = node1.get_left()
B.add_leaf(5)
node1 = B.get_root()
node1 = node1.get_left()
print(node1)
B.add_leaf(10)
node1 = B.get_root().get_right()
print(node1)
