class Solution:
    def getFactorial(self):
        num = int(input("Enter num : "))
        value = num
        factorial = 1

        while num > 0:
            factorial *= num
            num-=1

        print(f"Factorial of {value} is {factorial}")

solution_obj = Solution()
solution_obj.getFactorial()