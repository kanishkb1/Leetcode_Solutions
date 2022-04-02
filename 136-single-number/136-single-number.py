class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        list1 = list(set(nums))
        updated_list1 = list1*2
        return sum(updated_list1) - sum(nums)
        
       #Time complexity-O(n) 
       #Space Complexity- O(n)