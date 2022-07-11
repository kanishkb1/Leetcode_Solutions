class Solution:
    def findComplement(self, num: int) -> int:
        mask =0
        temp = num
        
        while temp:
            mask = (mask<<1) | 1
            temp = temp >> 1
        return mask ^ num
    
    #Time complexity- O(n)
    #Space complexity- O(1)
        