# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is a palindrome while 123 is not.

#LEVEL - EASY

class Solution:
    def isPalindrome(self, x: int) -> bool:
        o = x
        n = 0
        while x > 0:
            n = (n * 10) + (x % 10)
            x = x // 10
            
        return n == o
