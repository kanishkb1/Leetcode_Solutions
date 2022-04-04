class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        pointer1 = 0
        pointer2 = len(nums)-1
        while pointer1<pointer2:
            if nums[pointer1]==nums[pointer1+1]:
                return nums[pointer1]
            if nums[pointer2]==nums[pointer2-1]:
                return nums[pointer2]
            pointer1+=1
            pointer2-=1