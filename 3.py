class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxi = 0
        hs = set()
        le,ri = 0, 0
        while ri<len(s):
            while s[ri] in hs:
                hs.remove(s[le])
                le += 1
            maxi = max(maxi,ri-le+1)
            hs.add(s[ri])
            ri += 1
        return maxi
