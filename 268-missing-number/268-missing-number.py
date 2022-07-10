class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        #x1 -> represents XOR of all values from 1 to n
        x1 =1
        for i in range(2,n+1):
            x1 = x1 ^ i
        #x2 -> XOR of all values in nums    
        x2 = nums[0]
        for i in range(1,n):
            x2 = x2 ^ nums[i]
        #    
        return x1 ^ x2
    
    #Time complexity- O(n)
    #Space complexitry- O(1)