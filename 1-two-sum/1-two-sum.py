class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h={}
        for i,value in enumerate(nums):
            n=target-value
            if n not in h:
                h[value]=i
            else:
                return [h[n],i]
            
        