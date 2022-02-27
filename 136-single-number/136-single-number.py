class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums1 = sum(sorted(nums))
        nums2 = sum(list(set(nums)) * 2)
        return nums2- nums1
        
        #Time complexity- O(N)
        #Space complexity-O(N)