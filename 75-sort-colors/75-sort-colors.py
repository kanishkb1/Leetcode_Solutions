class Solution:
    def sortColors(self, nums: List[int]) -> None: 
        
        n = len(nums)
        #creating two pointers
        low = 0
        i=0
        
        high = n-1
        while i<=high:
            if nums[i]==0:
                nums[i],nums[low]=nums[low],nums[i]
                i+=1
                low+=1
        
            elif nums[i]==1:
                i+=1
            else:
                nums[i],nums[high]=nums[high],nums[i]
                high-=1
                
     