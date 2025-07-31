def subarrayBitwiseORs(arr) -> int:
    res = set()
    cur = set()
    for n in arr:
        newcur = {n | x for x in cur} | {n}
        res.update(newcur)
        cur = newcur
    return len(res)

print(subarrayBitwiseORs([0]))
print(subarrayBitwiseORs([1,1,2]))
print(subarrayBitwiseORs([1,2,4]))
