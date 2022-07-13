class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        low = 0
        high = n -1
        
        while low <= high:
            mid = low + (high - low) // 2
            if target < letters[mid]:
                high = mid -1
            else:
                low = mid + 1
        return letters[low % n]
    
    #Time complexity- O(log N)
    #Space Complexity- O(1)