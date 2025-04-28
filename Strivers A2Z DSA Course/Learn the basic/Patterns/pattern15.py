"""
A B C D E F G 
A B C D E F 
A B C D E 
A B C D 
A B C 
A B 
A 
"""


def nLetterTriangle(n: int) -> None:
    # Write your solution here.
    for i in range(n, 0, -1):
        char_val = 65
        for j in range(i, 0, -1):
            print(chr(char_val), end=" ")
            char_val += 1
        print()

nLetterTriangle(7)
