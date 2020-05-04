def compress(s):
  ans = ''
  counter = 0
  for index in range(len(s)):
    counter += 1
    if (index == len(s) - 1 or
        s[index] != s[index + 1]):
        ans += s[index] + f"{counter}"
        counter = 0

  return ans

print(compress('aaabbbgggsssqb'))