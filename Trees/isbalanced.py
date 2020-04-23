from binary_search_tree import *

def find_height(node):
  if (node == None):
    return 0
  left = find_height(node.left)
  right = find_height(node.right)
  if (left == -1 or right == -1):
    return -1
  
  diff = abs(left - right)
  if (diff > 1):
    return -1
  else:
    return max(left, right) + 1

def is_balanced(tree):
  return find_height(tree.root) != -1

tree = BinarySearchTree()
tree.add_leaf(10)
tree.add_leaf(5)
# tree.add_leaf(1)
tree.add_leaf(20)

print(is_balanced(tree))
