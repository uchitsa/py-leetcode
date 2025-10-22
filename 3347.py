class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        res = 0
        cnt = defaultdict(int)
        mds = set()

        def addmod(v):
            mds.add(v)
            if v-k >= nums[0]:
                mds.add(v-k)
            if v+k <= nums[-1]:
                mds.add(v+k)
        
        last = 0
        for i in range(len(nums)):
            if nums[i]!=nums[last]:
                cnt[nums[last]] = i-last
                res = max(res,i-last)
                addmod(nums[last])
                last = i
        
        cnt[nums[last]] = len(nums)-last
        res = max(res, len(nums)-last)
        addmod(nums[last])

        for m in sorted(mds):
            le = bisect.bisect_left(nums,m-k)
            ri = bisect.bisect_right(nums,m+k)-1
            if m in cnt:
                t = min(ri-le+1, cnt[m]+numOperations)
            else:
                t = min(ri-le+1, numOperations)
            res = max(res, t)
        return res
