class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        first_pointer=0
        second_pointer=n - 1
        while second_pointer>first_pointer:
            if nums[first_pointer]==nums[first_pointer+1]:
                return nums[first_pointer]
            if nums[second_pointer]==nums[second_pointer-1]:
                return nums[second_pointer]
            first_pointer+=1
            second_pointer-=1
                
        
        
        