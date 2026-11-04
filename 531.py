class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        m = len(picture[0])
        n = len(picture)
        rowcnt = [0] * n
        colcnt = [0] * m
        i = 0
        while i < n:
            j = 0
            while j < m:
                if picture[i][j] == 'B':
                    rowcnt[i] += 1
                    colcnt[j] += 1
                j += 1
            i += 1

        i = 0
        res = 0
        while i < n:
            j = 0
            while j < m:
                if picture[i][j] == 'B' and rowcnt[i] == 1 and colcnt[j] == 1:
                    res += 1
                j += 1
            i += 1

        return res

        
