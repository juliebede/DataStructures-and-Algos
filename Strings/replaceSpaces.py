def replaceSpaces(s, n):
  ans = [None for char in range(n)]
  index = n - 1
  
  while (index >= 0):
    char = s[index]
    if (char == ' '):
      ans[index] = '20%'
    else:
      ans[index] = char
    index -= 1

  return ''.join(ans)


print(replaceSpaces('Mr John Smith', 13))
print(replaceSpaces('  a  ', 5))