class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        i = 0
        j = len(s)-1
        sl = list(s)
        while i < j:
            if sl[i] not in vowels:
                i += 1
            elif sl[j] not in vowels:
                j -= 1
            else:
                sl[i], sl[j] = sl[j], sl[i]
                i += 1
                j -= 1
        return "".join(sl)
