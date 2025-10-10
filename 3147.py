class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        res = -inf
        for i in range(len(energy)-k,len(energy)):
            s = 0
            j=i
            while j>=0:
                s += energy[j]
                res = max(res,s)
                j-=k
        return res
