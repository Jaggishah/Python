class Solution:
    def isPalindrome(self, x: int) -> bool:
        k=str(x)
        pali=k[::-1]
        if k == pali:
            return True