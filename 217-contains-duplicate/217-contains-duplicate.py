class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #Using set data-type
        l1 = list(set(nums))
        if len(l1)==len(nums):
            return False
        else:
            return True
        #Space Complexity- O(N)
        #Time Complexity- O(N)