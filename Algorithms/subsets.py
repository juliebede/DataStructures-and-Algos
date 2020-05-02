
## design an algorithm to find all subsets of a set

def subsets(set, index, result, currentSub):
  if (index >= len(set)):
    return
  
  ## add the value
  newSub = currentSub + [set[index]]
  result.append(newSub)

  subsets(set, index + 1, result, currentSub)
  subsets(set, index + 1, result, newSub)


def findSubsets(set):
  result = [[]]
  subsets(set, 0, result, [])
  return result

print(findSubsets([1,2,3]))

## [] => [[]]
## [1 ,2 ,3] => [[],[1], [1,2], [1,2,3], [3], [2], [2,3]]   [3]