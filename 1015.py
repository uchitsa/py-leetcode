class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        rem = 1
        lenn = 1
        seen = set()
        while rem%k != 0:
            n = rem*10+1
            rem = n%k
            lenn += 1
            if rem in seen:
                return -1
            else:
                seen.add(rem)
        return lenn
