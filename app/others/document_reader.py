from pathlib import Path

path = f"{Path(__file__).parents[2]}\document"


def doc_reader(doc_name):
    with open(rf"{path}\{doc_name}.txt", "r", encoding="utf-8") as file:
        file_contents = file.read()

    return file_contents
