class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        le, ri = 0, 0
        highfreq, maxl = 0, 0
        freqs = {}
        for ri in range(len(s)):
            freqs[s[ri]] = freqs.get(s[ri], 0) + 1
            highfreq = max(highfreq, freqs[s[ri]])
            n2repl = ri-le+1-highfreq
            if n2repl > k:
                freqs[s[le]] -= 1
                le += 1
            maxl = ri-le+1
        return maxl
    
