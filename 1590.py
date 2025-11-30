class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums) % p
        if total == 0:
            return 0        
        mod_map = {0: -1}
        prefix_sum = 0
        min_len = len(nums)
        for i, num in enumerate(nums):
            prefix_sum = (prefix_sum + num) % p
            needed = (prefix_sum - total + p) % p
            if needed in mod_map:
                min_len = min(min_len, i - mod_map[needed])
            
            mod_map[prefix_sum] = i
        
        return min_len if min_len < len(nums) else -1
