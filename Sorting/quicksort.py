def partition(arr, left, right):
  pos = left
  while (pos <= right):
    if (arr[pos] <= arr[right]):
      temp = arr[left]
      arr[left] = arr[pos]
      arr[pos] = temp
      left += 1
    pos += 1

  return left - 1

def quicksort(arr, left, right):
  index = partition(arr, left, right)
  print(left, index)
  if (left < index):
    quicksort(arr, left, index - 1)
  if (right > index):
    quicksort(arr, index + 1, right)


array = [9,2,23,2,2,4,21,443,2,21,68,33] 
quicksort(array, 0, len(array) - 1)
print(array)