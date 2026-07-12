class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        neo = sorted(arr)
        ranks = {}
        rank = 1
        for i in range(len(neo)):
            if i>0 and neo[i]>neo[i-1]:
                rank += 1
            ranks[neo[i]] = rank
        for i in range(len(arr)):
            arr[i] = ranks[arr[i]]
        return arr
