class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        for i in range(0,n):
            nums[i] = nums[i] ** 2
            
        return sorted(nums)   
            