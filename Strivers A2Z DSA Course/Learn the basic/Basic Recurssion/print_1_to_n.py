"""
Print 1 to n
"""


def print_num(count, n):
    if count < 1:
        return
    print_num(count - 1, n)
    print(count)

n = 50
print_num(n, n)
