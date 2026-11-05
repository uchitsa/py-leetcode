class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        cnt = 0
        for x in arr1:
            i = bisect.bisect_left(arr2, x)
            flag = True
            if i < len(arr2) and abs(arr2[i] - x <= d):
                flag = False
            if i > 0 and abs(arr2[i - 1] - x) <= d:
                flag = False
            cnt += flag
        return cnt
