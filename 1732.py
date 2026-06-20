class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alts = [0] * (len(gain)+1)
        for i in range(1,len(gain)+1):
            alts[i] = alts[i-1] + gain[i-1]
        return max(alts)
