class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        digits = []

        while x > 0:
            digit = x % 10
            digits.append(digit)
            x = x // 10

        print(digits)

        for i in range(len(digits) // 2):
            if digits[i] != digits[-i - 1]:
                return False
        return True


number = 7521257

solution = Solution()
print(solution.isPalindrome(number))
