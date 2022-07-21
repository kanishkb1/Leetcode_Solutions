class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if not matrix or not matrix[0]:
            return False
        
        left = 0
        m = len(matrix) 
        n = len(matrix[0])
        
        for row in matrix:
            if row[0] <=target<=row[-1]:
                left = 0
                right = n - 1
                
                while left <=right:
                    mid =left + (right - left) // 2
                    mid_value = row[mid]
                    if target > mid_value:
                        left = mid + 1
                        
                    elif target < mid_value:
                        right = mid -1
                    else:
                        return True
        return False
    #TC: O(m log n)
    #SC: O(1)