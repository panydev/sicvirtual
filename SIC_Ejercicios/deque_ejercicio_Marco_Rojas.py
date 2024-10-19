class Deque:
    def __init__(self):
        self.__deque=["elemen", 12, 3, 4]

    def add_first(self, item):
        self.__deque.insert(0, item)

    def __str__(self):
        return f'Valores del deque: {self.__deque}'

    def remove_first(self):
        return None if len(self.__deque) == 0 else self.__deque.pop(0)

    def add_last(self, item):
        self.__deque.append(item)

    def remove_last(self):
        return None if len(self.__deque) == 0 else self.__deque.pop()

deque=Deque()
deque.add_first("a")
deque.add_first("b")
deque.add_last("c")
deque.remove_first()
deque.remove_last()
deque.add_first("b")
deque.remove_last()
print(deque)