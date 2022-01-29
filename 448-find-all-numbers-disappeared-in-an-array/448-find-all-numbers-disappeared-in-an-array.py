class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        nums =sorted(nums)
        nums1 = set(list(range(1,n+1)))
        nums2 = nums1.difference(nums)
        return nums2