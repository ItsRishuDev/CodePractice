"""
Print name n to 1 times
"""


def print_num(count, n):
    if count < 1:
        return
    print(count)
    print_num(count - 1, n)


n = 50
print_num(n, n)


# Usign Backtracking


def print_num(count, n):
    if count > n:
        return
    print_num(count + 1, n)
    print(count)


n = 50
print_num(1, n)
