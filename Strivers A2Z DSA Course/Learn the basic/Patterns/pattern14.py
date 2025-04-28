"""
A
A B
A B C
A B C D
A B C D E
A B C D E F
A B C D E F G
"""


def nLetterTriangle(n: int) -> None:
    # Write your solution here.
    for i in range(1, n + 1):
        char_val = 65
        for j in range(1, i + 1):
            print(chr(char_val), end=" ")
            char_val += 1
        print()

nLetterTriangle(7)
