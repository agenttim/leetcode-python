class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        prev_value = 0

        for char in s[::-1]:
            value = roman_to_int[char]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value

        return total

s = "MCMXCIV"
print(Solution().romanToInt(s))

#V 5 5 5
#I 1 4 1
#C 100 104 100
#X 10 94 10
#M 1000 1094 1000
#C 100 994 100
#M 1000 1994 1000




