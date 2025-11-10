class Solution:
    def minOperations(self, nums: List[int]) -> int:
        st = []
        res = 0
        for n in nums:
            while st and st[-1]>n:
                st.pop()
            if n == 0:
                continue
            if not st or st[-1]<n:
                res += 1
                st.append(n)
        return res
        
