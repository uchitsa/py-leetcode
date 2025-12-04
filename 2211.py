class Solution:
    def countCollisions(self, directions: str) -> int:
        res = 0
        b = -1
        for d in directions:
            if d=='L':
                if b>=0:
                    res += b+1
                    b = 0
            elif d=='S':
                if b>0:
                    res += b
                b = 0
            else:
                if b>=0:
                    b+=1
                else:
                    b = 1
        return res
        
