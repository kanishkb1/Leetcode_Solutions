class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        n = len(height)
        #two pointers 
        pointer1 = 0
        pointer2 = n -1
        current_water_level=0
        while pointer1<pointer2:
            current_water_level = max(current_water_level, (pointer2-pointer1) * min(height[pointer1],height[pointer2]))
            if height[pointer1]<height[pointer2]:
                pointer1 += 1 
            else:
                pointer2 -= 1
        return current_water_level
    
    #Time complexity- O(n)
    #Space complexity- O(1) as no extra space is used.