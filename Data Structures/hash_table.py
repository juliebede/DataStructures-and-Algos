class Node():

  def __init__(self, item):
    self.item = item
    self.next = None


def hash_example(arr):
  table = [None, None, None, None]
  for element in arr:
    new_node = Node(element)
    new_node.next = table[element]
    table[element] = new_node
  
  print(table)


hash_example([1,2,3])