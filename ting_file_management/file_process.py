from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance: Queue):
    # Verifica se o arquivo já foi processado.
    for item in instance.queue:
        if item["nome_do_arquivo"] == path_file:
            print(f"Arquivo '{path_file}' já foi processado.")
            return

    # Importa o conteúdo do arquivo.
    linhas_arquivo = txt_importer(path_file)
    if not linhas_arquivo:
        return
    # Cria o dicionário com os dados do arquivo.
    dados_arquivo = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(linhas_arquivo),
        "linhas_do_arquivo": linhas_arquivo,
    }

    # Adiciona o dicionário à fila.
    instance.enqueue(dados_arquivo)

    # Mostra os dados processados no stdout.
    print(f"\n{dados_arquivo}")


def remove(instance: Queue):
    # Verifica se a fila está vazia.
    if instance.__len__() == 0:
        return print("Não há elementos")

    # Remove o primeiro arquivo da fila.
    file_removed = instance.dequeue()

    # Mostra a mensagem de sucesso.
    print(f"Arquivo {file_removed['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance: Queue, position):
    # Verifica se a posição é válida.
    if position < 0 or position >= len(instance):
        print("Posição inválida", file=sys.stderr)
        return

    # Recupera o arquivo da fila.
    arquivo = instance.search(position)

    # Mostra as informações do arquivo.
    print(f"\n{arquivo}")

    # OUTRA FORMA DE FAZER O MESMO PROCESSO
    # try:
    #     queue_data = instance.search(position)
    #     print(queue_data)
    # except IndexError:
    #     return print("Posição inválida", file=sys.stderr)
