def reorderedPowerOf2(n: int) -> bool:
    return any(val[0] != "0" and bin(int("".join(val))).count("1") == 1 for val in itertools.permutations(str(n)))

print(reorderedPowerOf2(2))
print(reorderedPowerOf2(1))
print(reorderedPowerOf2(0))
print(reorderedPowerOf2(1024))
print(reorderedPowerOf2(-1))
