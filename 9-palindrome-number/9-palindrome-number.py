class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        rev_str=str_x[::-1]
        if rev_str == str_x:
            return True