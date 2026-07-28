class Solution:
    def smallestPalindrome(self, s: str) -> str:
        p = len(s)//2
        one = sorted(s[:p])
        mid = [s[p]] if len(s)%2==1 else []
        two = one[::-1]
        return "".join(one+mid+two)
