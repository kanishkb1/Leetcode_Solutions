class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n=len(nums)
        low = 0
        high= n - 1
        
        if len(nums)==1:
            if nums[0]!=target:
                return False
            else:
                return True
        
        
        
        while low<=high:
            mid = (low + high) // 2
            
            if nums[mid]==target:
                return True
            
            elif nums[low]==nums[mid]==nums[high]:
                low+=1
                high-=1
            
            elif nums[low] <= nums[mid]:
                if nums[low] <= target <nums[mid]:
                    high = mid - 1
                else:
                    low=mid+1
                  
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                    
                else:
                    high= mid - 1
        return False      
    
    #Space Complexity- O(log n)
    #Time complexity- O(1)
    
                 