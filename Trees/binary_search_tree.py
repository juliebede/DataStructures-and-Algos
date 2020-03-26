class Node():

  def __init__(self, item, left, right):
    self.item = item
    self.left = left
    self.right = right

class BinarySearchTree():

  def __init__(self):
    self.root = None

  def is_empty(self):
    return self.root == None

  def add_leaf(self, item):
    if (self.is_empty):
      self.root = Node(item, None, None)
    else:
      current = self.root
      while (current != None):
        