class Solution:
    def isPalindrome(self, s: str) -> bool:
        sumStr = ""
        for i in s:
            if i.isalnum():
                sumStr += i.lower()
        return sumStr == sumStr[::-1]