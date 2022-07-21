class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        
        
        left = 0
        right = len(matrix ) * len(matrix[0])
        
        while left < right:
            mid = (left + right) // 2
            i = mid // len(matrix[0])
            j = mid % len(matrix[0])
            
            if matrix[i][j] == target:
                return True
            
            elif matrix[i][j]> target:
                right = mid
                
            else:
                left = mid+1
                
        return False
