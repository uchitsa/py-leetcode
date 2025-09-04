def findClosest(x: int, y: int, z: int) -> int:
  minx = abs(z-x)
  miny = abs(z-y)
  if minx<miny:
      return 1
  elif miny<minx:
      return 2
  else:
      return 0

print(findClosest(2,7,4))
print(findClosest(2,5,6))
print(findClosest(1,5,3))
