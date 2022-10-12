class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        length = len(nums)
        
        start=0
        end = length - 1
        
        while start < end:
            mid = (end + start) // 2
            if nums[mid] > nums[mid + 1]:
                end = mid
            else:
                start = mid + 1
        return start
    
    #TC: O(log n)
    #SC:O(1)