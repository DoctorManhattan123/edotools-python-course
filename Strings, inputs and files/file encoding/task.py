def fix_encoding(filename: str):
    # Convert file to windows encoding, you can assume that the
    # file is in utf-8 encoding
    with open(filename, encoding="cp1252") as file:
        content = file.read()

    print(content)

    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)


# this file was mistakenly opened with windows encoding
with open("example.txt", "r", encoding="cp1252") as file:
    content = file.read()

# now the content looks broken (look in the example.txt)
with open("example.txt", "w", encoding="utf-8") as file:
    file.write(content)
