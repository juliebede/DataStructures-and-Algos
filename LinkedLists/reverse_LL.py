from LinkedList import *

## reversing a linked list
def reverse_linked_list(L):

  prev = None  # this will be assigned as the new next
  curr = L    # this is the node we are reassigning next
  next = None  # this is the next node we wil work on

  while (curr != None):

    # store the next value
    next = curr.next

    # reassign current.next to previous (reverses)
    curr.next = prev

    # set previous to current to work on the next one
    prev = curr
    # assign curr to next to work on the next node
    curr = next

  return prev



LL = Node(1)
LL.next = Node(2)
LL.next.next = Node(3)
LL.next.next.next = Node(4)
reversedLL = reverse_linked_list(LL)
print(reversedLL)
print(reversedLL.next)
print(reversedLL.next.next)
print(reversedLL.next.next.next)
print(reversedLL.next.next.next.next)

