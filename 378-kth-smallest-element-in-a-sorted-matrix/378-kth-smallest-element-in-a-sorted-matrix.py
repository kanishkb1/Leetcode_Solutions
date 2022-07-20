class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        
        #2D pointers for 2D  array
        left = matrix[0][0]
        right = matrix[n-1][n-1]
        
        while left<right:
            mid = left + (right - left) // 2
            total = 0
            
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    if matrix[i][j]<=mid:
                        total+=1
                        
            if total < k:
                left = mid + 1
                        
            else:
                right = mid
                        
        return left