class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        st = set()
        for i in range(1,len(nums)):
            summ = nums[i]+nums[i-1]
            if summ in st:
                return True
            st.add(summ)
        return False
