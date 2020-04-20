def paint(screen, x, y, color):
  print(x, y)
  if (x < 0 or y < 0 
      or x >= len(screen[0]) or y >= len(screen)):
    return screen
  elif (screen[y][x] != color):
    screen[y][x] = color
    paint(screen, x, y + 1, color)
    paint(screen, x, y - 1, color)
    paint(screen, x + 1, y, color)
    paint(screen, x - 1, y, color)

  return screen

print(paint([["yellow", "green", "yellow"], ["green", "yellow", "green"], ["green", "green", "green"]], 
      2, 1, "yellow"))
