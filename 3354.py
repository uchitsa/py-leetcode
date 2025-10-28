class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        cnt = 0
        n = len(nums)
        zeroidx = [i for i in range(n) if nums[i]==0]
        for i in zeroidx:
            for direct in (-1,1):
                arr = nums[:]
                cur = i
                dir = direct
                while 0 <= cur < n:
                    if arr[cur]==0:
                        cur += dir
                    else:
                        arr[cur] -= 1
                        dir = -dir
                        cur += dir
                if all(x==0 for x in arr):
                    cnt += 1
        return cnt
