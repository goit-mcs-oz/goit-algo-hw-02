
# Завдання 1

from dataclasses import dataclass, field
from queue import Queue


@dataclass
class Request:
    _counter: int = 0
    id: int = field(init=False)

    def __post_init__(self):
        type(self)._counter += 1
        self.id = type(self)._counter


queue = Queue()


def generate_request():
    request = Request()
    queue.put(request)


def process_request():
    if not queue.empty():
        request = queue.get()
        print(f"Обробка заявки {request.id}")
    else:
        print("Черга пуста")


def main():
    while True:
        cmd = input(
            "Натисни Enter, щоб створити/обробити заявку, або 'q' для виходу: ").strip().lower()
        if cmd == "q":
            print("Вихід із програми.")
            break

        generate_request()
        process_request()


main()
