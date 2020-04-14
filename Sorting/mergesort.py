def merge(beg, end, L):
  i, j, k = 0, 0, 0
  while (i < len(beg) and j < len(end)):
    if (beg[i] < end[j]):
      L[k] = beg[i]
      i += 1
    else:
      L[k] = end[j]
      j += 1
    k += 1
  
  while (j < len(end)):
    L[k] = end[j]
    k, j = k + 1, j + 1
  while (i < len(beg)):
    L[k] = beg[i]
    i, k = i + 1, k + 1  

  return L

def mergesort(arr):
  if (len(arr) == 1):
    return arr
  else:
    beginning = mergesort(arr[:len(arr) // 2])
    end = mergesort(arr[len(arr) // 2:])
    return merge(beginning, end, arr)


print(mergesort([38, 27, 43, 9]) == [9, 27, 38, 43])