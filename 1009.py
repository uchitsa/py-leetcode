class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        x, b = n, 1
        while x:
            n = n ^ b
            b = b << 1
            x = x >> 1
        return n
