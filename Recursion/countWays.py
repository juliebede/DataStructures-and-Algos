def count_DP(n, map):
  if (n < 0):
    return 0
  elif (n == 0):
    return 1
  elif (n in map):
    return map[n]
  else:
    return count_DP(n - 1, map) + count_DP(n - 2, map) + count_DP(n - 3, map)


def count_ways(n):
  return count_DP(n, {})

print(count_ways(5))