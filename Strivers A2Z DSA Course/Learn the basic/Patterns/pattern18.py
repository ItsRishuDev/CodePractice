"""
C
C B
C B A
"""


def alphaTriangle(n: int):
    # Write your solution here.

    for i in range(1, n + 1):
        char_val = 64 + n
        for _ in range(i):
            print(chr(char_val), end=" ")
            char_val -= 1
        print()


alphaTriangle(5)
