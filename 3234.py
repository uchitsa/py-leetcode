class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        pr = [-1]*(n+1)
        for i in range(n):
            if i==0 or s[i-1]=='0':
                pr[i+1]=i
            else:
                pr[i+1]=pr[i]
        res = 0
        for i in range(1,n+1):
            cnt0=1 if s[i-1]=='0' else 0
            j=i
            while j>0 and cnt0*cnt0<=n:
                cnt1 = (i-pr[j])-cnt0
                if cnt0*cnt0 <= cnt1:
                    res += min(j-pr[j],cnt1-cnt0*cnt0+1)
                j = pr[j]
                cnt0 += 1
        return res
        
