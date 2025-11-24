# Завдання 2

from collections import deque
import string


def is_palindrome(str: string):
    symbols = "".join(str.split()).lower()
    d = deque()
    for s in symbols:
        d.append(s)
    while d:
        if len(d) == 1:
            return True
        left_symbol = d.popleft()
        right_symbol = d.pop()
        if left_symbol != right_symbol:
            return False
    return True


print(is_palindrome("level"))
