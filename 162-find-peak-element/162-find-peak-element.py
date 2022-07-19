class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start = 0
        n = len(nums)
        end = n -1
        
        while end > start:
            mid = start + (end - start) // 2
            if nums[mid] > nums[mid + 1]:
                end = mid
                
            else:
                start = mid + 1
            
        return start
            #Time complexity- O(log n)
            #Space complexity- O(1)