"""
    A
  A B A
A B C B A
"""


def alphaHill(n: int):
    # Write your solution from here.
    for i in range(1, n + 1):
        char_val = 65
        print("  " * (n - i), end="")
        for j in range(1, i + 1):
            print(chr(char_val), end=" ")
            char_val += 1
        char_val -= 1
        for k in range(i - 1):
            char_val -= 1
            print(chr(char_val), end=" ")
        print()


alphaHill(7)
