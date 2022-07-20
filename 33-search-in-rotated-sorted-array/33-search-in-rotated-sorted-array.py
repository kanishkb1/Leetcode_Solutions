class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low = 0
        high = n - 1
        
        if not nums:
            return -1
        
        while low <= high:
            mid = (low + high) // 2
            
            if target==nums[mid]:
                return mid 
            
            if  nums[low] <= nums[mid]:  
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
                    
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
    
    #TC: O(log n)
    #SC: O(1)
                