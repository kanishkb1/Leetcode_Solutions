class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result =  0
        for num in nums:
            result ^= num
        return result
    #Time complexity- O(n)
    #Space Complexity-O(1)