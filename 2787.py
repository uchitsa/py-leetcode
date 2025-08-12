def numberOfWays(n: int, x: int) -> int:
    mod = 10**9+7
    k = 0
    while (k+1)**x<=n:
        k += 1
    dp = [0]*(n+1)
    dp[0] = 1
    for i in range(1,k+1):
        v = i**x
        for s in range(n,v-1,-1):
            dp[s]=(dp[s]+dp[s-v])%mod
    return dp[n]%mod

print(numberOfWays(10,2))
print(numberOfWays(4,1))
    
