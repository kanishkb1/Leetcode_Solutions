class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num = 0
        for i in nums:
            
            num = num ^ i
            print(num)
        return num
    
    #Space Complexity- O(1)
    #Time complexity- O(n)