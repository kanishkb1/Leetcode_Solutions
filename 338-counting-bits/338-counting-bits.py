class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0]
        for i in range(1,n+1):
            result.append(result[i >> 1] + i % 2)
        return result
        
      #Space-complexity- O(n)
      #Time complexity- O(n)