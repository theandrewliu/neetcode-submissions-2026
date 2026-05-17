class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        h = {}
        for num in nums:
            if num in h:
                h[num] += 1
            else: 
                h[num] = 1
            if h[num] > 1:
                return True
        return False