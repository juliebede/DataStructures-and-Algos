def isRotation(S1, S2):
  if (len(S1) != len(S2)):
    return False

  S2 = S2 + S2
  if (S1 in S2):
    return True

  return False

print(isRotation('waterbottle', 'erbotetlewat'))