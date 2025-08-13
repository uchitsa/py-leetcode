def isPowerOfThree(n: int) -> bool:
  if n<1:
      return False
  r = log(n)/log(3)
  return abs(r-round(r))<0.0000000001

print(isPowerOfThree(0))
print(isPowerOfThree(1))
print(isPowerOfThree(2))
print(isPowerOfThree(3))
print(isPowerOfThree(27))
