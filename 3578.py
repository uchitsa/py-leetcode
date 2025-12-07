class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        n=len(nums)
        mod=10**9+7
        d=[0]*(n+1)
        pr=[0]*(n+1)
        cnt=SortedList()
        d[0]=1
        pr[0]=1
        j=0
        for i in range(n):
            cnt.add(nums[i])
            while j<=i and cnt[-1]-cnt[0]>k:
                cnt.remove(nums[j])
                j+=1
            d[i+1]=(pr[i]-(pr[j-1]if j>0 else 0))%mod
            pr[i+1]=(pr[i]+d[i+1])%mod
        return d[n]
