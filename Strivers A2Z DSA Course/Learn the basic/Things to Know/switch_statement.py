"""
Get day Name
"""

class Solution:
    def getDayName(self):
        get_age = True
        while get_age:
            try:
                age = int(input("Enter your age : "))
                if age < 1:
                    print("Invalid age provided")
                else:
                    get_age = False
            except ValueError:
                print("Invalid age provided")
        if age >= 18:
            print("You are an adult.")
        else:
            print("You are not an adult.") 

solution_obj = Solution()
solution_obj.checkAdult()
