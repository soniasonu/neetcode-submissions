class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        num = x
        result = 0
        while x > 0:
            id = x % 10
            result = (result * 10) + id
            x = x // 10
        return num == result