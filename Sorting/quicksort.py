def partition(arr, left, right):
  pivot = arr[right]
  i = 0
  j = 0
  while (j < right):
    if (arr[j] <= pivot):
      arr[i],arr[j] = arr[j], arr[i]
      i += 1
    
    j += 1
  
  arr[i], arr[right] = arr[right], arr[i]
  
  return i

def quicksort(arr, left, right):
  pivot = partition(arr, left, right)
  if (left < pivot - 1):
    quicksort(arr, left, pivot - 1)
  if (pivot + 1 < right):
    quicksort(arr, pivot + 1, right)


array = [9,2,23,2,2,4,21,443,2,21,68,500] 
quicksort(array, 0, len(array) - 1)
print(array)
