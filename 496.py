class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        st = []
        hsm = {}
        for n in nums2:
            while st and n > st[-1]:
                hsm[st.pop()] = n
            st.append(n)
        return [hsm.get(i, -1) for i in nums1]
