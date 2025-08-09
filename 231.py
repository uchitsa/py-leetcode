def isPowerOfTwo( n: int) -> bool:
  if n <= 0:
      return False
  p = log(n)/log(2)
  return abs(p - round(p)) < 0.0000000001

print(isPowerOfTwo(2147483647))
print(isPowerOfTwo(0))
print(isPowerOfTwo(2))
