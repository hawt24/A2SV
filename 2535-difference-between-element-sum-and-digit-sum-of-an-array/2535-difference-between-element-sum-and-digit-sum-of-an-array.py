class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        digit = 0
        for number in nums:
            number_string = str(number)
            for digit_char in number_string:
                digit += int(digit_char)
        return abs(sum(nums) - digit)