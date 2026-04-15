class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        res, n = len(words), len(words)
        for i, w in enumerate(words):
            if w==target:
                di = abs(i-startIndex)
                res = min(res, min(di, n-di))
        if res<n:
            return res
        return -1
