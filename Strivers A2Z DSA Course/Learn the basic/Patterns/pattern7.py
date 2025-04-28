"""
  *
 ***
*****
"""


def nStarTriangle(n: int) -> None:
    for i in range(1, n + 1):
        print(" " * (n - i), end="")
        print("*" * (i), end="")
        print("*" * (i - 1))


nStarTriangle(68)
