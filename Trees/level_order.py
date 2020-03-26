from binary_search_tree import *


def level_order_traversal(t):
  node_items = []
  current_level_nodes = [t.root]
  for node in current_level_nodes:
    if (node != None):
      node_items.append(node.item)
      current_level_nodes.append(node.get_left())
      current_level_nodes.append(node.get_right())
  return node_items


tree = BinarySearchTree()
tree.add_leaf(30)
tree.add_leaf(10)
tree.add_leaf(40)
tree.add_leaf(5)
tree.add_leaf(20)
tree.add_leaf(35)
print(level_order_traversal(tree))
tree2 = BinarySearchTree()
print(level_order_traversal(tree2))


