class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        biglen = len(word1) if len(word1) >= len(word2) else len(word2)
        merged = ""
        while i < biglen:
            if i < len(word1):
                merged += word1[i]
            if i < len(word2):
                merged += word2[i]
            i += 1
        return merged
