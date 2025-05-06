"""
Given an integer array nums, return the greatest common divisor of the smallest number and largest number in nums.

The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.

Example 1:

Input: nums = [2,5,6,9,10]
Output: 2
Explanation:
The smallest number in nums is 2.
The largest number in nums is 10.
The greatest common divisor of 2 and 10 is 2.
Example 2:

Input: nums = [7,5,6,8,3]
Output: 1
Explanation:
The smallest number in nums is 3.
The largest number in nums is 8.
The greatest common divisor of 3 and 8 is 1.

"""


class Solution:
    def findGCD(self, nums: list[int]) -> int:
        min_num = min(nums)
        max_num = max(nums)

        gcd = 1

        for i in range(1, min_num + 1):
            if min_num % i == 0 and max_num % i == 0:
                gcd = i

        return gcd


# Optimize Solution


class Solution:
    def findGCD(self, nums: list[int]) -> int:
        min_num = min(nums)
        max_num = max(nums)

        while min_num != 0:
            max_num = max_num - min_num
            if max_num < min_num:
                min_num, max_num = max_num, min_num
        return max_num
