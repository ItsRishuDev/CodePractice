"""
Given an integer N, print all the divisors of N in the ascending order.


Example 1:

Input : 20
Output: 1 2 4 5 10 20
Explanation: 20 is completely
divisible by 1, 2, 4, 5, 10 and 20.

Example 2:

Input: 21191
Output: 1 21191
Explanation: As 21191 is a prime number,
it has only 2 factors(1 and the number itself).

Your Task:

Your task is to complete the function print_divisors() which takes N as input parameter and prints all the factors of N as space seperated integers in sorted order. You don't have to print any new line after printing the desired output. It will be handled in driver code.
"""


class Solution:
    def print_divisors(self, N):
        # code here
        result = set()
        for i in range(1, N + 1):
            if N % i == 0:
                rem = int(N / i)
                if rem in result:
                    break
                result.add(i)
                result.add(rem)

        for i in sorted(result):
            print(i, end=" ")
