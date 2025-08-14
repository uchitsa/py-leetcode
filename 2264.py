from collections import Counter
def largestGoodInteger(num: str) -> str:
    maxi = 0
    res = ""
    counts = Counter(num)
    for k, v in counts.items():
        if v >= 3:
            s = k*3
            if s in num:
                if int(s)>=maxi:
                    maxi = int(s)
                    res = s
    return res

print(largestGoodInteger("6777133339"))
print(largestGoodInteger("2300019"))
print(largestGoodInteger("42352338"))
