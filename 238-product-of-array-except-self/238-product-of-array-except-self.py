class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Using postfix sum/product and suffix sum/product
        n=len(nums)
        res = [1]*n
        prefix = 1
        n=len(nums)
        for i in range(n):
            res[i] = prefix
            prefix*= nums[i]
            
        postfix=1
        for i in range(n-1,-1,-1):
            res[i]*=postfix
            postfix*=nums[i]
        return res
      
    
    #Time complexity- O(n)
    #Space Complexity- O(1)