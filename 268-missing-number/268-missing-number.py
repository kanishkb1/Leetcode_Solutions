class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n =len(nums)
        nums = sorted(nums)
        return sum(range(0,n+1)) - sum(nums)
    
    #Time complexity- O(1)
    #Space complexity- O(n)
    
    
        
        