"""
  *
 ***
*****
*****
 ***
  *
"""


def nStarDiamond(n: int) -> None:
    for i in range(1, n + 1):
        print(" " * (n - i), end="")
        print("*" * (i), end="")
        print("*" * (i - 1))
    for i in range(n, 0, -1):
        print(" " * (n - i), end="")
        print("*" * (i), end="")
        print("*" * (i - 1))


nStarDiamond(3)
