from LinkedList import *


def removeDups(root):
  if (root == None):
    return None

  start = root
  set = []
  set.append(root.val)

  while (root != None and root.next != None):
    if (root.next.val in set):
      root.next = root.next.next
    else:
      set.append(root.next.val)

    root = root.next
  
  return start


l = Node(1)
l.next = Node(2)
l.next.next = Node(2)
l.next.next.next = Node(3)
print(removeDups(l))
