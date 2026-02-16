class Solution:
    def reverseBits(self, n: int) -> int:
        res, pwr = 0, 31
        while n:
            res += (n&1)<<pwr
            n = n >> 1
            pwr -= 1
        return res
        
