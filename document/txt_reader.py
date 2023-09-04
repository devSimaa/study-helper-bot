def reader_txt(import_txt):
    with open(import_txt, "r", encoding="utf-8") as file:
        text = file.read()
    return text
