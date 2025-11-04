class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        res = []
        for i in range(n-k+1):
            cnt = Counter(nums[i:i+k])
            frq = sorted(cnt.items(),key=lambda item:(-item[1], -item[0]))
            xs = sum(k*v for k,v in frq[:x])
            res.append(xs)
        return res
