"""
1
1 2
1 2 3
"""


def nTriangle(n: int) -> None:
    # Write your solution here.
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
