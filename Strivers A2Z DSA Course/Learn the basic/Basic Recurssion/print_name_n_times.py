"""
Print name n times
"""


def print_name(count, n):
    if count == n:
        return
    print("Shri Radha")
    print_name(count + 1, n)


print_name(0, 500)
