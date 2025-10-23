class Solution:
    def hasSameDigits(self, s: str) -> bool:
        x = list(s)
        n = len(s)
        for i in range(1,n-1):
            for j in range(n-i):
                dig1=ord(x[j])-ord('0')
                dig2=ord(x[j+1])-ord('0')
                x[j]=chr(((dig1+dig2)%10)+ord('0'))
        return x[0]==x[1]
    
