def makeTheIntegerZero(num1: int, num2: int) -> int:
    k = 1
    while True:
        x = num1 - num2*k
        if x < k:
            return -1
        if k >= x.bit_count():
            return k
        k += 1

print(makeTheIntegerZero(3,-2))
print(makeTheIntegerZero(5,7))
