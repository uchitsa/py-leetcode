class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        li = [False] * (len(strs)-1)
        res = 0
        for s in zip(*strs):
            if all(li[i] or s[i]<=s[i+1] for i in range(len(s)-1)):
                for i in range(len(s)-1):
                    if s[i]<s[i+1]:
                        li[i] = True
            else:
                res += 1
        return res
