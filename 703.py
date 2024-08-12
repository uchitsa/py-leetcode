import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minheap = []
        self.k = k
        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        if len(self.minheap) < self.k or self.minheap[0] < val:
            heapq.heappush(self.minheap, val)
            if len(self.minheap) > self.k:
                heapq.heappop(self.minheap)
        return self.minheap[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
