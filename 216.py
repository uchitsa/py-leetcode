class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        res = []

        def bkt(acc, start, pathsum):
            if len(acc) == k:
                if pathsum == n:
                    res.append(acc[:])
                return
            if pathsum > n:
                return
            for num in range(start,10):
                acc.append(num)
                bkt(acc, num + 1, pathsum + num)
                acc.pop()

        bkt([], 1, 0)
        return res
