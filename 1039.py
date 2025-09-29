class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [0]*n
        for i in range(n):
            dp[i] = [0]*n
        for lng in range(3,n+1):
            for i in range(0,n-lng+1):
                j = i + lng - 1
                dp[i][j]= math.inf
                for k in range(i+1,j):
                    sco = dp[i][k]+dp[k][j] + values[i]*values[k]*values[j]
                    dp[i][j] = min(dp[i][j],sco)
        return dp[0][n-1]
