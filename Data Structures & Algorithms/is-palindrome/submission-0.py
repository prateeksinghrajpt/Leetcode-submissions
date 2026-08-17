class Solution:
    def isPalindrome(self, s: str) -> bool:
        q=""
        for ch in s:
            if ch.isalnum():
                q += ch.lower()
        return q==q[::-1]
        
        