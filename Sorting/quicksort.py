def partition(arr, left, right):
  pivot = arr[(left + right) // 2]
  while (left <= right):

    while (arr[left] < pivot):
      left += 1
    
    while (arr[right] > pivot):
      right -= 1

    if (left <= right):
      temp = arr[left]
      arr[left] = arr[right]
      arr[right] = temp
      left += 1
      right -= 1
    
  return left

def quicksort(arr, left, right):
  index = partition(arr, left, right)
  if (left < index - 1):
    quicksort(arr, left, index - 1)
  if (index < right):
    quicksort(arr, index, right)


array = [9,2,23,2,2,4,21,443,2,21,68,500] 
quicksort(array, 0, len(array) - 1)
print(array)