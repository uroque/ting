def exists_word(word, instance):
    result = []

    for item in instance._queue:
        occurrences = []

        for index, line in enumerate(item["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                occurrences.append({"linha": index + 1})

        if len(occurrences) > 0:
            result.append({
                "palavra": word,
                "arquivo": item['nome_do_arquivo'],
                "ocorrencias": occurrences
            })

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
