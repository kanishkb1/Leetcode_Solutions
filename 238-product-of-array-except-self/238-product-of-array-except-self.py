class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Using postfix sum/product and suffix sum/product
        n=len(nums)
        output = [1]*n
        
        #Prefix product part
        for i in range(0,n):
            if i!=0:
                output[i] = output[i-1] * nums[i-1]
                
        #Suffix product part
        post = nums[n-1]
        for i in range(n-1,0,-1):
            output[i-1] = output[i-1] * post
            post = post * nums[i-1]
            
        return output
    
    #Time complexity- O(n)
    #Space Complexity- O(n)