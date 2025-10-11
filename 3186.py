class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        from collections import Counter
        cnt = Counter(power)
        dmgs = sorted(cnt.keys())
        n = len(dmgs)
        dp = [0]*(n+1)
        for i in range(1,n+1):
            dp[i] = dp[i-1]
            curdmg = dmgs[i-1]
            total = cnt[curdmg]*curdmg
            j = i-1
            while j>0 and dmgs[j-1] >= curdmg - 2:
                j -= 1
            dp[i] = max(dp[i], total+dp[j])
        return dp[n]
