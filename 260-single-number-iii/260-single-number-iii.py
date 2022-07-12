class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        n1xn2 = 0
        
        #get XOR of all number
        for num in nums:
            n1xn2 = n1xn2 ^ num
        
        # get the rightmost bit that is '1'
        rightmost_set_bit = 1
        while rightmost_set_bit & n1xn2 == 0:
            rightmost_set_bit = rightmost_set_bit << 1
        num1, num2 = 0,0
        
        
        for num in nums:
            if num & rightmost_set_bit != 0:
                num1 ^= num
            else:
                num2 ^= num
                
        return [num1,num2]
        #Time complexity- O(n)
        #Space complexity- O(1)
                       

        
        