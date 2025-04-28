"""
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21
22 23 24 25 26 27 28
"""


def nNumberTriangle(n: int) -> None:
    # Write your solution here.
    count = 0
    for i in range(1, n + 1):
        for _ in range(1, i + 1):
            count += 1
            print(count, end=" ")
        print()


nNumberTriangle(7)
