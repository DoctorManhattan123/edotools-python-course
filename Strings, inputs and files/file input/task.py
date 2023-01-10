def open_and_print():
    # Open the file and return the file contents to stdout
    file = open("example.txt")
    content = file.read()
    file.close()
    return content


def open_and_double():
    # Open the file, copy the content, and append the content
    # Use the correct flag

    with open("example.txt", "r") as file:
        content = file.read()

    with open("example.txt", "a") as file:
        file.write(content)
