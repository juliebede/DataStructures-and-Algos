def unique_chars(s):
  s = ''.join(sorted(s))
  i = 0
  while (i < len(s) - 1):
    if (s[i] == s[i + 1]):
      return False
    i += 1
  return True


print(unique_chars('abc'))