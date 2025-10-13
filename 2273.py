class Solution:
    from collections import Counter
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = [words[0]]
        n = len(words)

        def cmp(w1,w2)->bool:
            frq = [0]*26
            for c in w1:
                frq[ord(c)-ord('a')] += 1
            for c in w2:
                frq[ord(c)-ord('a')] -= 1
            return all(x==0 for x in frq)
        
        for i in range(1,n):
            if cmp(words[i],words[i-1]):
                continue
            res.append(words[i])
        return res
        
