class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def squar(a,b,c):
            return 0.5 * abs(a[0]*b[1]+b[0]*c[1]+c[0]*a[1] 
            - a[1]*b[0]-b[1]*c[0]-c[1]*a[0])
        return max(squar(*triag) for triag in itertools.combinations(points,3))
      
