


def find_rotated_list(a, target):
  start = 0
  end = len(a) - 1

  while (start < end):
    middle = (start + end) // 2

    if (a[middle] == target):
      return middle

    elif (a[start] < a[middle]):
      if (a[start] < target < a[middle]):
        end = middle - 1
      else:
        start = middle + 1
    
    elif (a[middle] < a[end]):
      if (a[middle] < target < a[end]):
        start = middle + 1
      else:
        end = middle - 1
    
    else:
      start += 1
      end += 1
    
  return False

print(find_rotated_list([15, 16,  19, 20, 25, 1, 3, 4, 5, 7, 10, 14], 5))
print(find_rotated_list([2, 2, 2, 2, 3, 4, 5, 2], 5))
print(find_rotated_list([2, 2, 2, 2, 3, 2, 2, 2], 3))