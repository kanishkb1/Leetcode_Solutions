class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        
        #edge cases
        if n==0: 
            return sum(nums)
        if n==1:
            return sum(nums)
        global_max = -999999
        local_max =0
        for i in range(0,n):
            local_max = max(nums[i],nums[i]+local_max)
            if local_max > global_max:
                global_max = local_max
        return global_max
    
    #Space complexity- O(n)
    #Time complexity- O(1)