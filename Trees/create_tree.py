from binary_search_tree import *

def create(A):
  if (len(A) == 0):
    return None
  mid = len(A) // 2
  n = Node(A[mid], None, None)
  n.left = create(A[:mid])
  n.right = create(A[mid + 1:])
  return n

def create_tree(A):
  new_tree = BinarySearchTree()
  new_tree.root = create(A)
  return new_tree


tree = create_tree([1,2,3,4,5])
print(tree.root.right)