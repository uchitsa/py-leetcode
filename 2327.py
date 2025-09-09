def peopleAwareOfSecret(n: int, delay: int, forget: int) -> int:
    mod = 10**9+7
    dp = [0]*(n+1)
    dp[1] = 1
    canshare = 0
    for i in range(2, n+1):
        if i-delay>=1:
            canshare = (canshare+dp[i-delay])%mod

        if i-forget>=1:
            canshare = (canshare-dp[i-forget]+mod)%mod
        
        dp[i] = canshare
    
    start = max(1, n-forget+1)
    total = sum(dp[start:n+1])%mod

    return total

print(peopleAwareOfSecret(6,2,4))
print(peopleAwareOfSecret(4,1,3))
