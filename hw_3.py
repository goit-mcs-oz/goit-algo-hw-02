# Завдання 3

import string


class Stack:
    def __init__(self):
        self.stack = []

    # Додавання елемента до стеку
    def push(self, item):
        self.stack.append(item)

    # Видалення елемента зі стеку
    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    # Перевірка, чи стек порожній
    def is_empty(self):
        return len(self.stack) == 0

    # Перегляд верхнього елемента стеку без його видалення
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]


brackets_s = ["(", ")"]
brackets_sq = ["[", "]"]
brackets_c = ["{", "}"]


def get_brackets_by_symbols(symbols):
    if symbols in brackets_s:
        return brackets_s
    if symbols in brackets_sq:
        return brackets_sq
    if symbols in brackets_c:
        return brackets_c


def check_string(str: string):
    symbols = "".join(str.split()).lower()
    stack = Stack()
    added_open_symbol = ''
    brackets = None
    for s in symbols:
        if s == brackets_s[0] or s == brackets_sq[0] or s == brackets_c[0]:
            stack.push(s)
            added_open_symbol = s
        if s == brackets_s[1] or s == brackets_sq[1] or s == brackets_c[1]:
            brackets = get_brackets_by_symbols(added_open_symbol)
            if s != brackets[1]:
                return "Несиметрично"
            stack.pop()
    if stack.is_empty():
        return "Симетрично"
    else:
        return "Несиметрично"


print(check_string("( ){[ 1 ]( 1 + 3 )( ){ }}"))
