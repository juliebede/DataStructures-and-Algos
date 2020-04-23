from binary_search_tree import *

def check(node, visited):
  if (node == None):
    return None
  
  check(node.left, visited) ## adds each node in order in the visited list
  if (len(visited) > 0 and
      node.item < visited[-1]):
    return False

  visited.append(node.item)
  
  right = check(node.right, visited)
  if (right == False):
    return False
  
  return node.item


def isBST(node):
  return check(node, []) != False

new = Node(10, None, None)
new.left = Node(5, None, None)
new.left.right = Node(25, None, None)

print(isBST(new))