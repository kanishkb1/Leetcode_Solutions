class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        r= s.split()
        n= len(r)
        return len(r[n-1])