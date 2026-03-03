class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        cnt = 0
        lng = (1<<n)-1
        while k>1:
            if k == lng//2+1:
                return "1" if cnt%2==0 else "0"
            if k>lng//2:
                k = lng+1-k
                cnt += 1
            lng //= 2
        return "0" if cnt%2==0 else "1"
        
