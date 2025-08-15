def isPowerOfFour(n: int) -> bool:
    if n<=0:
        return False
    r = log(n)/log(4)
    return abs(r-round(r))<0.0000000001

print(isPowerOfFour(16))
print(isPowerOfFour(5))
print(isPowerOfFour(1))
