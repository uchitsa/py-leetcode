class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        prefcomm = [0]*n
        for cur in range(n):
            comc = 0
            for aid in range(cur+1):
                for bid in range(cur+1):
                    if A[aid] == B[bid]:
                        comc += 1
                        break
            prefcomm[cur] = comc
        return prefcomm
            
