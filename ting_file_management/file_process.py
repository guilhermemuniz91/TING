from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer


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
    """Aqui irá sua implementação"""


def file_metadata(instance: Queue, position):
    """Aqui irá sua implementação"""
