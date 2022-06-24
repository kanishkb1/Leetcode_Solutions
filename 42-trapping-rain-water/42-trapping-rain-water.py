class Solution:
    def trap(self, height: List[int]) -> int:
        left=0
        right= len(height) - 1
        
        area =0
        left_max=0
        right_max=0
        
        while left<right:
            left_max=max(left_max,height[left])
            right_max=max(right_max,height[right])
            
            if height[left] < height[right]:
                area = area + left_max - height[left]
                left=left+1
                
            else:
                area = area + right_max - height[right]
                right=right-1
                
        return area
        #Space complexity - O(1) as no extra space is used.
        #Time complexity- O(n)
        