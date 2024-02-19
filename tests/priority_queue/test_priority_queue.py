from ting_file_management.priority_queue import PriorityQueue
import pytest


mock_qtd_linhas = [9, 4, 2, 5, 7, 11, 3]

mock_data = [
    {
        "nome_do_arquivo": f"arquivo{index+1}.txt",
        "qtd_linhas": mock_qtd_linhas[index],
        "linhas_do_arquivo": [
            f"linha{index_linha+1}"
            for index_linha in range(mock_qtd_linhas[index])
        ],
    }
    for index in range(len(mock_qtd_linhas))
]


def test_basic_priority_queueing():
    priority_queue = PriorityQueue()
    for data in mock_data:
        priority_queue.enqueue(data)

    assert priority_queue.__len__() == len(mock_data)

    assert priority_queue.search(6) == mock_data[5]

    assert priority_queue.dequeue() == mock_data[1]
    assert priority_queue.dequeue() == mock_data[2]
    assert priority_queue.dequeue() == mock_data[6]
    assert priority_queue.dequeue() == mock_data[0]

    with pytest.raises(IndexError):
        priority_queue.search(7)
