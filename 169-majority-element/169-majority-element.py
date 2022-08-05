class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        half = n // 2
    
        nums = sorted(nums)
        return nums[half]
        