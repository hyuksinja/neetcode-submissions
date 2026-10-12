class Solution:
    def isPalindrome(self, s: str) -> str:
        l=""
        for ch in s:
            if ch.isalnum():
                l=l+ch.lower()
        if l==l[::-1]:
            return True
        else:
            return False
        