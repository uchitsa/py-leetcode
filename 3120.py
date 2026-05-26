class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        st = set(word)
        cnt = 0
        cnt += sum(c in st and c.upper() in st for c in string.ascii_lowercase)
        return cnt
