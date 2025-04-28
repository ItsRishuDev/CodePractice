"""
Check the age of the user
"""

class Solution:
    def getDayName(self):
        day = int(input("Enter day : "))
        
        match day:
            case 1:
                return "Monday"
            case 2:
                return "Tuesday"
            case 3:
                return "Wednesday"
            case 4:
                return "Thursday"
            case 5:
                return "Friday"
            case 6:
                return "Saturday"
            case 7:
                return "Sunday"
            case default:
                return "Invalid Day"


solution_obj = Solution()
print(solution_obj.getDayName())
