class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums))==len(nums):
            return False
        else:
            return True
    #Space Complexity- O(n)
    #Time complexity- O(n)
