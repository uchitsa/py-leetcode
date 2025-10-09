class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n, m = len(skill), len(mana)
        t = [0] * n
        for j in range(m):
            curt = 0
            for i in range(n):
                curt = max(curt, t[i]) + skill[i] * mana[j]
            t[n - 1] = curt
            for i in range(n - 2, -1, -1):
                t[i] = t[i + 1] - skill[i + 1] * mana[j]
        return t[n - 1]
