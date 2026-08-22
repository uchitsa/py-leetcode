class Solution:
    def checkDivisibility(self, n: int) -> bool:
        summ = 0
        prod = 1
        neo = n
        while neo>9:
            summ += neo%10
            prod *= neo%10
            neo //= 10
        summ += neo
        prod *= neo
        if n%(summ+prod)==0:
            return True
        return False
