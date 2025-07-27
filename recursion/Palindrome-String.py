class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s="".join(reversed(s))
        if s==new_s:
            return True
        return False