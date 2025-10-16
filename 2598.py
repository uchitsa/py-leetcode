class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        m = Counter(x % value for x in nums)
        mex = 0
        while m[mex%value]>0:
            m[mex%value] -= 1
            mex += 1
        return mex
