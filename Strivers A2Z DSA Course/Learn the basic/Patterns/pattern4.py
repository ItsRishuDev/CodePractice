"""
1
2 2
3 3 3
4 4 4 4
"""


def triangle(n: int) -> None:
    # Write your solution here.
    for i in range(1, n + 1):
        print(f"{i} " * i)
