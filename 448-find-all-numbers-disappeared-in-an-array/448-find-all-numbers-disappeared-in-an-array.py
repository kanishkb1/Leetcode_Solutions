class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s1 = set(nums)
        s2=set(range(1,len(nums)+1))
        return s2.difference(s1)
    
    #Time complexity- O(n)
    #Space Complexity-O(n)
        
        
        
        