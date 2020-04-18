class Node:

  def __init__(self, val):
    self.val = val 
    self.par = None
    self.height = 0
    self.right = None
    self.left = None

  def __str__(self):
    return f"{self.val}"


class AVLTree:

  def __init__(self):
    self._root = None
  
  def get_root(self):
    return self._root

  def add_node(self, val):
    new_node = Node(val)
    curr = self._root
    if (curr == None):
      self._root = new_node
    else:
      while (curr != None):
        curr.height += 1
        if (val < curr.val):
          if (curr.left == None):
            curr.left = new_node
            new_node.par = curr
            curr = None
          else:
            curr = curr.left
        else:
          if (curr.right == None):
            curr.right = new_node
            new_node.par = curr
            curr = None
          else:
            curr = curr.left


T = AVLTree()
T.add_node(7)
node = T.get_root()
print(node)
T.add_node(3)
T.add_node(1)
node1 = node.left
node2 = node1.left
print(node1, node2)
