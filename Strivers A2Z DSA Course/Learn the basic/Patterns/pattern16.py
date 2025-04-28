"""
A
B B
C C C
D D D D
"""


def alphaRamp(n: int) -> None:
    # Write your solution from here.
    char_val = 65
    for i in range(1, n + 1):
        print(f"{chr(char_val)} " * i)
        char_val += 1


alphaRamp(4)
