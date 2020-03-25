# Selection sort, continuing finding small elements and adding it in order

def selection_sort(arr):
  length = len(arr)
  for index in range(0, length):
    current_min = index
    for index2 in range(index, length):
      if (arr[index2] < arr[current_min]):
        current_min = index2
    temp = arr[current_min]
    arr[current_min] = arr[index]
    arr[index] = temp
  
  return arr


print(selection_sort([10, 7, 1, 200, 30, 130])) 