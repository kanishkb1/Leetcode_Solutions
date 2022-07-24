class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #initialization of two pointer
        left=0
        n=len(nums)
        right=n - 1
        
        #left will be incremented and right will be decremented.
        while left <= right:
            if nums[left] + nums[right] ==target:
                return [left,right]
            right-=1
            
            if left==right:
                left+=1
                right=n-1
            #Time complexity- O(n)
            #Space complexity- O(1) as no extra meory is used
                
            
        