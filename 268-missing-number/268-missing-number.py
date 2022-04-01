class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        return sum(range(n+1)) - sum(sorted(nums))
       #Runtime complexity- O(1)
       #Space complexity- O(n)