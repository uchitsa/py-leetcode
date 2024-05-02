class Solution:
    def decodeString(self, s: str) -> str:
        return self.concat(s, 0)[0]

    def concat(self, s: str, i: int):
        res = ""
        while i < len(s) and s[i] != ']':
            if s[i].isalpha():
                part, i = self.letters(s, i)
                res += part
            elif s[i].isdigit():
                part, i = self.mult(s, i)
                res += part
            else:
                i += 1
        return res, i

    def mult(self, s: str, i: int):
        num, i = self.number(s, i)
        i += 1
        part, i = self.concat(s, i)
        i += 1
        return part * num, i

    def number(self, s: str, i: int):
        end = i
        while end < len(s) and s[end].isdigit():
            end += 1
        return int(s[i:end]), end

    def letters(self, s: str, i: int):
        end = i
        while end < len(s) and s[end].isalpha():
            end += 1
        return s[i:end], end


if __name__ == '__main__':
    sol = Solution()
    print(sol.decodeString("3[a]2[bc]"))
    print(sol.decodeString("3[a2[c]]"))
    print(sol.decodeString("2[abc]3[cd]ef"))
