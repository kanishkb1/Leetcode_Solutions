class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #initialization of two pointer
        left=0
        n=len(nums)
        right=n - 1
        
        #left will be incremented and right will be decremented.
        while left <= right:
            if nums[left] + nums[right] == target:
                return [left,right]
            right=right-1
            
            if right==left:
                left+=1
                right=n-1
            
            
      
        