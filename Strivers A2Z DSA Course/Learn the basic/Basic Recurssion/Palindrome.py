class Solution:
    def isPalindrome(self, s: str) -> bool:
        ns = ""
        for i in s:
            if i.isalnum():
                ns += i.lower()

        return True if ns == ns[::-1] else False
