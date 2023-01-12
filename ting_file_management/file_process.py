import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    file = txt_importer(path_file)

    content = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file,
    }

    if content in instance._queue:
        return None

    instance.enqueue(content)
    sys.stdout.write(str(content))
    return content


def remove(instance):
    if len(instance) == 0:
        sys.stdout.write("Não há elementos\n")
        return None

    else:
        removed_content = instance.dequeue()["nome_do_arquivo"]
        sys.stdout.write(f"Arquivo {removed_content} removido com sucesso\n")
        return None


def file_metadata(instance, position):
    try:
        metadata = instance.search(position)
        sys.stdout.write(str(metadata))
        return None

    except IndexError:
        sys.stderr.write("Posição inválida\n")
        return None
