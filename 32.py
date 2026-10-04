class Solution:
    def longestValidParentheses(self, s: str) -> int:
        st = []
        for i, c in enumerate(s):
            if c == ')' and st and s[st[-1] ]== '(':
                st.pop()
            else:
                st.append(i)
        st.append(len(s))
        maxi = st[0]
        for i in range(1, len(st)):
            maxi = max(maxi, st[i]-st[i-1]-1)
        return maxi
      
