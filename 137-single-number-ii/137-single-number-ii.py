class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        b = 0
        for x in nums:
            a,b = (~x & a & ~b ) | (x & ~a & b), ~a & (x ^ b)
        return b
            
            