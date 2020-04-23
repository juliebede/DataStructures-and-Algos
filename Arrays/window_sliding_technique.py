
## use this technique to find the max sum of k consecutive elements
## ex) [5, 2, -1, 0, 3] k = 3 ==> 6 (5 + 2 + -1)

def find_max_subarray(arr, k):
  if (len(arr) < k):
    return -1

  max_so_far = sum(arr[:k])
  
  window_sum = max_so_far
  prev = 0
  next_index = k

  while (next_index < len(arr)):
    window_sum = window_sum - arr[prev] + arr[next_index]
    max_so_far = max(window_sum, max_so_far)

    prev += 1
    next_index += 1
  
  return max_so_far

# print(find_max_subarray([], 1))
print(find_max_subarray([5, 2, -1, 0, 3], 3))