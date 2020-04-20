from binary_search_tree import Node
class LL_Node():

  def __init__(self, val):
    self.val = val
    self.next = None
  
  def __str__(self):
    return f"{self.val}"

# class Linked_list():

#   def __init__(self):
#     self.start = None
# def create_level(r, elements):
#   if (len(elements) == 0):
#     return 
#   curr = LL_Node(0)
#   new = []
#   for e in elements:
#     curr.next = LL_Node(e.item)
#     curr = curr.next
#     if (e.left != None):
#       new.append(e.left)
#     if (e.right != None):
#       new.append(e.right)
#   print(curr)
#   create_level(r, new)
    

# def create_lists(t):
#   results = []
#   create_level(results, [t])
#   return results



def create_level_linked_list(root, lists, level):
  if (root == None):
    return 
  if (len(lists) == level): ## if the level has not been reached
    list = LL_Node(root.item)
    lists.append(list)
  else:
    list = lists[level]
    new = LL_Node(root.item)
    new.next = list
    list = new
    lists[level] = list
  create_level_linked_list(root.left, lists, level + 1)
  create_level_linked_list(root.right, lists, level + 1)

def create_linked_list(root):
  lists = []
  create_level_linked_list(root, lists, 0)
  return lists


tree = Node(1, None, None)
tree.left = Node(2, None, None)
tree.right = Node(3, None, None)

r = create_linked_list(tree)
print(r[1].next)
