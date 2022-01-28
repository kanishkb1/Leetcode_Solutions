class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        nums=sorted(nums)
        return sum(list(range(0,n+1))) - sum(nums)
    #Space Complexity- O(1)
    #Time complexity- O(n)
        
        
        