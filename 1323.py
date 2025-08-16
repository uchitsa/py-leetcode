def maximum69Number(num: int) -> int:
    s = str(num)
    return int(s.replace('6','9',1))

print(maximum69Number(9669))
print(maximum69Number(9996))
print(maximum69Number(9999))
