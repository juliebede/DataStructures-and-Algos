# arr => a sorted list
# target => a number within the sorted list

# Searching through the list to find a number by constantly dividing
# O(logN)

def binary_search(arr, target):
  beg = 0
  end = len(arr) - 1
  while (beg <= end):
    middle = (beg + end) // 2
    if (arr[middle] == target):
      return True
    elif (target < arr[middle]):
      end = middle - 1
    elif (target > arr[middle]):
      beg = middle + 1

  return False

print(binary_search([1,2,3], 2)) ## true
print(binary_search([4, 10, 23, 23, 23, 40, 90, 10000, 20000], 4)) # false
print(binary_search([4, 10, 23], 11)) # true
