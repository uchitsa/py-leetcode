class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        modd = 10**9+7
        cnt = prefs = 0
        oddcnt = 0
        evencnt = 1
        for n in arr:
            prefs += n
            if prefs % 2 == 0:
                cnt += oddcnt
                evencnt += 1
            else:
                cnt += evencnt
                oddcnt += 1
            cnt %= modd
        return cnt
