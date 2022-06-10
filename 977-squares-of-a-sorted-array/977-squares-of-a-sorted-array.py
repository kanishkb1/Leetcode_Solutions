class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        #declaration of two pointers
        left = 0 
        right = n - 1
        i = len(nums)-1
        ans = [0]*n
        
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                ans[i] = nums[left] **2
                left+=1
                
            else:
                ans[i] = nums[right] ** 2
                right-=1
            i-=1   
        return ans
        
    
            