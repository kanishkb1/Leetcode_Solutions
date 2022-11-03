class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        size = len(arr)    
        for i in range(0,size-1):
            arr[i] = max(arr[i+1:])
        arr[-1] = -1
        
        return arr
    