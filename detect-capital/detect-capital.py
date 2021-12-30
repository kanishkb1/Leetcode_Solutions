class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        for i in range(len(word)):
            if word.isupper():
                return True
            elif word.islower():
                return True
            elif word.istitle():
                return True