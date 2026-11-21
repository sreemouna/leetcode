class Solution:
    def isPalindromic(self, s: str) -> bool:
        bin =""

        for ch in s:
            bin += format(ord(ch),'08b')

        return bin == bin[::-1]
        