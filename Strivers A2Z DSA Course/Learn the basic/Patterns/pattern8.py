"""
*****
 ***
  *
"""


def nStarTriangle(n: int) -> None:
    for i in range(n, 0, -1):
        print(" " * (n - i), end="")
        print("*" * (i), end="")
        print("*" * (i - 1))


nStarTriangle(55)
