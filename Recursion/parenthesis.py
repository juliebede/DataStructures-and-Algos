def parenthesis(n):

  ## Base case to start 
  if (n == 0):
    return [""]
  
  combos = [] ## stores all the combos for n
  prev = parenthesis(n - 1) ## get combos for n - 1 to work with

  ## loops through previous combo and adds to it
  for string in prev:
    beside = "()" + string
    ends = "(" + string + ")"
    combos.append(beside)
    if (n != 1):
      combos.append(ends)

    otherside = string + "()"
    if (otherside not in combos):
      combos.append(otherside)
  return combos


print("results:", parenthesis(4))