class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        length = len(nums)
        
        nums.sort()
        
        return nums[length // 2]
    
    #Time complexity- O(n)
    #Space Complexity- O(1)