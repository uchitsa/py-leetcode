class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"(":")", "{":"}", "[":"]"}
        st = []
        for c in s:
            if c == "{" or c == "(" or c == "[":
                st.append(c)
                continue
            if c == "}" or c == ")" or c == "]":
                if st and c == pairs[st[-1]]:
                    st.pop()
                else:
                    return False
        if len(st) != 0:
            return False
        return True

if __name__ == '__main__':
    print(isValid("()"))
    print(isValid("()[]{}"))
    print(isValid("(]"))
