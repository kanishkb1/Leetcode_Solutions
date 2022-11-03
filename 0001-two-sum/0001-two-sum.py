class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #
        left=0
        n=len(nums)
        right=n - 1
        
  #
        while left <= right:
            if nums[left] + nums[right] == target:
                return [left,right]
            right=right-1
            
            if right==left:
                left+=1
                right=n-1
            
            
      
        