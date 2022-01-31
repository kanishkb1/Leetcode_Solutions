from functools import lru_cache
class Solution:
    def climbStairs(self, n: int) -> int:
        #EDGE CASES
        if n == 1:
            return 1
        if n==2:
            return 2
        
        #recursion using an array    
        res = [0 for i in range(n)]
        res[0], res[1] = 1, 2
        for i in range(2, n):
            res[i] = res[i-1] + res[i-2]
        return res[-1]
    
    #Space Complexity-O(n)
    #Time complexity- O(n*N)
            