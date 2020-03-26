class Multiset: 

  ## Initialized state
  def __init__(self):
    self.items = []

  def __str__(self):
    return f'{self.items}'

  def add(self, item):
    self.items.append(item)

  def delete(self, item):
    self.items.remove(item)

  

M = Multiset()
M.add(10)
M.add(12)
print(M)