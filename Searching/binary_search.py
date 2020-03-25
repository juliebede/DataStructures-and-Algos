# arr => a sorted list
# target => a number within the sorted list

def binary_search(arr, target):
  beginning = 0
  end = len(arr)
  while (end > beginning):
    middle = (beginning + end) // 2
    if (arr[middle] == target):
      return True
    elif (target > middle):
      beginning = middle + 1
    else:
      end = middle - 1
  
  return False

print(binary_search([1,2,3], 2)) ## true
print(binary_search([4, 10, 23, 23, 23, 40, 90, 10000, 20000], 4))
print(binary_search([4, 10, 23], 11))