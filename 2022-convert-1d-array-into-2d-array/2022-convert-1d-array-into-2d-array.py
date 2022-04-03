class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        arr = []
        if m*n != len(original):
            return []
        else:
            for i in range(0,m*n,n):
                arr.append(original[i:n+i])
            return arr
        #Space Complexity-O(n)
        #Time complexity-O(n^2)
        