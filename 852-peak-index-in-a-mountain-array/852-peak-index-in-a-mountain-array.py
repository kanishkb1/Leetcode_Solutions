class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        low = 0
        high = n -1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if arr[mid - 1] < arr[mid] > arr[mid+1]:
                return mid
            
            if arr[mid - 1] < arr[mid]:
                low = mid + 1
                
            else:
                high = mid 
        return arr[mid]
        #Time complexity- O(log N)
        #Space Complexity- O(1) as no extra space is used.