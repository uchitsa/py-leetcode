class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        s = 1
        mon = 1
        while n>0:
            for i in range(min(n,7)):
                total += mon + i
            n-=7
            mon+=1
        return total
