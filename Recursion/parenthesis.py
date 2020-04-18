def parenthesis(n):

  ## Base case to start 
  if (n == 0):
    return [""]
  
  combos = [] ## stores all the combos for n
  prev = parenthesis(n - 1) ## get combos for n - 1 to work with

  ## loops through previous combo and adds to it
  for string in prev:
    beside = "()" + string
    combos.append(beside)
    otherside = string + "()"
    if (otherside not in combos):
      combos.append(otherside)
    ends = "(" + string + ")"
    if (ends not in combos):
      combos.append(ends)

  return combos


print("results:", parenthesis(4))