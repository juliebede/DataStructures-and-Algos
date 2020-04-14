def merge(beg, end):
  new_arr = [];
  i = 0
  j = 0
  while (i < len(beg) and j < len(end)):
    if (beg[i] < end[j]):
      new_arr.append(beg[i])
      i += 1
    else:
      new_arr.append(end[j])
      j += 1
  
  if (i == len(beg) and j < len(end)):
    new_arr += end[j:]
  
  elif (i < len(beg) and j == len(end)):
    new_arr += beg[i:]
  
  return new_arr

def mergesort(arr):
  if (len(arr) == 1):
    return arr
  else:
    beginning = mergesort(arr[:len(arr) // 2])
    end = mergesort(arr[len(arr) // 2:])
    return merge(beginning, end)


print(mergesort([38, 27, 43, 9]) == [9, 27, 38, 43])