class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        see = {(0,0)}
        pq = [(grid[0][0],0,0)]
        res=0
        while pq:
            d,r,c=heapq.heappop(pq)
            res = max(res,d)
            if r==c==n-1:
                return res
            for cr,cc in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
                if 0<=cr<n and 0<=cc<n and (cr,cc) not in see:
                    heapq.heappush(pq, (grid[cr][cc],cr,cc))
                    see.add((cr,cc))
