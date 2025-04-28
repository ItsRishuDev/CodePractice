"""
*
**
***
**
*
"""


def nStarTriangle(n: int) -> None:
    # Write your code here.
    for i in range(n):
        print("*" * (i + 1))
    for i in range(n - 1, 0, -1):
        print("*" * i)


nStarTriangle(3)
