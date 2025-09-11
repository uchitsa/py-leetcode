def sortVowels(self, s: str) -> str:
    def isvowel(c):
        return c == 'a' or c == 'e' or c == 'o' or c == 'u' or c == 'i' or c == 'A' or c == 'E' or c == 'O' or c == 'U' or c == 'I'

    tmp = ""
    for c in s:
        if isvowel(c):
            tmp += c
    
    stmp = ''.join(sorted(tmp))
    j = 0
    res = ""
    for i in range(len(s)):
        if isvowel(s[i]):
            res += stmp[j]
            j += 1
        else:
            res += s[i]
    return res


print(sortVowels("lEetc0de))
