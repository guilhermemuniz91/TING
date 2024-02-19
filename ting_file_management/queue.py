from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.queue = list()

    def __len__(self):
        return len(self.queue)

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        # Se não houver mais itens na fila, o método retornará None
        if len(self.queue) == 0:
            return None
        # O método pop remove e retorna o valor do índice fornecido
        return self.queue.pop(0)

    def search(self, index):
        if 0 <= index < len(self.queue):
            return self.queue[index]
        raise IndexError("Índice Inválido ou Inexistente")
