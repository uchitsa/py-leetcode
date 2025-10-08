from sortedcontainers import SortedList
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        res = [1]*len(rains)
        sl = SortedList()
        m = {}
        for i, r in enumerate(rains):
            if r==0:
                sl.add(i)
            else:
                res[i]=-1
                if r in m:
                    it = sl.bisect(m[r])
                    if it==len(sl):
                        return []
                    res[sl[it]]=r
                    sl.discard(sl[it])
                m[r]=i
        return res
