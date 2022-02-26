class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n =len(nums)
        nums1 = set(sorted(nums))
        nums2 = set(list(range(1,n+1)))
        return nums2.difference(nums1)
    #Run complexity- O(n)
    #Time complexity- O(n)
        
        
        