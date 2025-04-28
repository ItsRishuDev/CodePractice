"""
1             1
1 2         2 1
1 2 3     3 2 1
1 2 3 4 4 3 2 1
"""


def numberCrown(n: int) -> None:
    # Write your solution here.
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print(" " * 4 * (n - i), end="")
        for k in range(i, 0, -1):
            print(k, end=" ")
        print()


numberCrown(4)
