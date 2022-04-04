class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        n=len(nums)
        p1=0
        p2=1
        output =[]
        for i in range(0,n-1):
            if nums[p1]==nums[p2]:
                output.append(nums[p2])
            else:
                p1 = p2
            p2+=1
        return output
        
        
                