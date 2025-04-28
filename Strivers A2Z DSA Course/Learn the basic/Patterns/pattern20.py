"""
*         *
* *     * *
* * * * * *
* *     * *
*         *
"""


def symmetry(n: int):
    # Write your solution from here.
    for i in range(1, n + 1):
        print("* " * i, end="")
        print("  " * 2 * (n - i), end="")
        print("* " * i, end="")
        print()
    for i in range(n - 1, 0, -1):
        print("* " * i, end="")
        print("  " * 2 * (n - i), end="")
        print("* " * i, end="")
        print()


symmetry(6)
