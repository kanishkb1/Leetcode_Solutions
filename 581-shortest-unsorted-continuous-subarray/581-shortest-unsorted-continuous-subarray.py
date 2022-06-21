class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        low = 0
        high = len(nums) - 1
        
        while low<len(nums)-1 and nums[low]<=nums[low+1]:
            low+=1
        
        if low==len(nums)-1:
            return 0
        
        while high>0 and nums[high]>=nums[high-1]:
            high-=1
            
        
        subarray_max = max(nums[low:high+1])
        subarray_min = min(nums[low:high+1])
        
        
        while low>0 and nums[low-1] > subarray_min:
            low-=1
            
        while high < len(nums)-1 and nums[high+1]< subarray_max:
            high+=1
            
        return high-low+1
    
    #Space complexity- O(1) as no extra space is used.
    #Time complexity- O(N) 