class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #To sort the the given nums
        sorted_nums = sorted(set(nums))
        if len(sorted_nums)==len(nums):
            return False
        else:
            return True
        #Runtime complexity- O(N)
        #Space Complexity- O(N)