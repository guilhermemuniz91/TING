from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.__data = list()

    def __len__(self):
        return len(self.__data)

    def enqueue(self, value):
        self.__data.append(value)

    def dequeue(self):
        if len(self.__data) == 0:
            return None
        return self.__data.pop(0)

    def search(self, index):
        if 0 <= index < len(self.__data):
            return self.__data[index]
        raise IndexError("Índice Inválido ou Inexistente")
