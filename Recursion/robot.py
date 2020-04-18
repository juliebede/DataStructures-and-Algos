def count(x, y, arr):
  print(arr)
  if (arr[x][y] != 0):
    return arr[x][y]
  if (y != 0):
    up = count(x, y - 1, arr)
    arr[x][y] += up
  if (x != 0):
    down = count(x - 1, y, arr)
    arr[x][y] += down
  return arr[x][y]
  

def robot(x, y):
  arr = [[0 for col in range(y)] for row in range(x)]
  arr[0][0] = 1
  return count(x - 1, y - 1, arr)

print(robot(3,2))