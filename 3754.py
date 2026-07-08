class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0
        st = ""
        summ = 0
        for c in str(n):
            if c != '0':
                st += c
                summ += int(c)
        return int(st) * summ
