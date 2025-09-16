import math
def replaceNonCoprimes(nums: List[int]) -> List[int]:
    stk = []
    for n in nums:
        stk.append(n)
        while len(stk)>=2:
            a = stk[-2]
            b = stk[-1]
            g = math.gcd(a,b)
            if g==1:
                break
            stk.pop()
            stk.pop()
            lcm = a*b//g
            stk.append(lcm)
    return stk

print(replaceNonCoprimes([6,4,3,2,7,6,2]))
