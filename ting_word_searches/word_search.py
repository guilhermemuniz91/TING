from ting_file_management.queue import Queue


# def line_ocurrences_report(line: int, content: str, show_cont: bool = False):
#     if show_cont:
#         return {"linha": line + 1, "conteudo": content}
#     return {"linha": line + 1}


def exists_word(word: str, instance: Queue):
    # Lista para armazenar os resultados da busca.
    resultados = []

    # Itera sobre os arquivos da fila.
    for arquivo in instance.queue:
        um_resultado = {
            "palavra": word,
            "arquivo": arquivo["nome_do_arquivo"],
            "ocorrencias": [],
        }
        # Itera sobre as linhas do arquivo.
        for i, linha in enumerate(arquivo["linhas_do_arquivo"]):
            # Verifica se a palavra está presente na linha.
            if word.lower() in linha.lower():
                # Adiciona o resultado à lista.
                um_resultado["ocorrencias"].append({"linha": i + 1})
        if len(um_resultado["ocorrencias"]) > 0:
            resultados.append(um_resultado)

    # Retorna a lista de resultados.
    return resultados


def search_by_word(word: str, instance: Queue):
    return exists_word(word, instance)
