"""
4444444
4333334
4322234
4321234
4322234
4333334
4444444
"""


def getNumberPattern(n: int) -> None:
    for i in range(1, n):
        for j in range(1, i + 1):
            print(f"{n-j+1}", end="")
        print(f"{n - i + 1}" * (2 * (n - i) - 1), end="")
        for j in range(i, 0, -1):
            print(f"{n-j+1}", end="")
        print()

    for i in range(n, 0, -1):
        end = i if i == n else i + 1
        for j in range(1, end):
            print(f"{n-j+1}", end="")
        print(f"{n - i + 1}" * (2 * (n - i) - 1), end="")
        for j in range(i, 0, -1):
            print(f"{n-j+1}", end="")
        print()


getNumberPattern(4)
