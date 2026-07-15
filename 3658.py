class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        odds, evens = 0, 0
        od = 1
        ev = 2
        for _ in range(n):
            odds += od
            od += 2
            evens += ev
            ev += 2
        lo = odds if odds<evens else evens
        gcd = 1
        for i in range(1,int(lo/2)+1):
            if odds%i==0 and evens%i==0:
                gcd = i
        return gcd
