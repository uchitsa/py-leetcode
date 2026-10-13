class Solution:
    def minStoneSum(self, piles: list[int], k: int) -> int:
        maxheap = [-pile for pile in piles]
        heapify(maxheap)

        for _ in range(k):
            heappush(maxheap, floor(heappop(maxheap) // 2))

        sum = 0
        while maxheap:
            sum += -heappop(maxheap)
        return sum
