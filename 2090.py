class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums
        n = len(nums)
        res = [-1] * n
        winsz = 2*k+1
        prefs = [0]*n
        prefs[0] = nums[0]
        for i in range(len(nums)):
            prefs[i] = nums[i] + prefs[i-1]

        for i in range(k, n-k):
            left = i-k
            right = i+k
            winsum = prefs[right]
            if left > 0:
                winsum -= prefs[left-1]
            res[i] = winsum // winsz
        return res
