"""
1
0 1
1 0 1
0 1 0 1
"""


def nBinaryTriangle(n: int) -> None:
    # Write your solution here.
    for i in range(1, n + 1):
        count = 0 if i % 2 == 0 else 1
        for j in range(1, i + 1):
            print(count % 2, end=" ")
            count += 1
        print()


nBinaryTriangle(5)
