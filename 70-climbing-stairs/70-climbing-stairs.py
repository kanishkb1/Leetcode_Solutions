from functools import lru_cache
class Solution:
    def climbStairs(self, n: int) -> int:
       #edge cases
        if n==1: 
            return 1
        if n==2: 
            return 2
        
        #recursion using an array   
        #current item is sum of previous two numbers
        current  = [0 for i in range(n)]
        current[0]=1
        current[1]=2
        
        for i in range(2,n):
            current[i] = current[i-1] + current[i-2]
        return current[-1]
    #Space complexity- O(n)
    #Time complexity- O(n*N)