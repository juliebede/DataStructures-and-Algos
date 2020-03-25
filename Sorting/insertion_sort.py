# insertion sort 

def insert(arr, pos):
  while (pos > 0 and arr[pos] < arr[pos - 1]):
    temp = arr[pos]
    arr[pos] = arr[pos - 1]
    arr[pos - 1] = temp
    pos -= 1

def insertion_sort(arr):
  for i in range(0, len(arr)):
    insert(arr, i)
  return arr

print(insertion_sort([5, 8, 2, 4]))