class Solution:
    def smallestNumber(self, n: int) -> int:
        x = 1
        while True:
            x = x*2
            if x>n:
                break
        return x-1
        
