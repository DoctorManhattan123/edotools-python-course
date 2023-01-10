def list_all_chars(text: str):
    # "text" -> ['t', 'e', 'x', 't']
    result = []
    for c in text:
        result.append(c)
    return result


def print_every_word_in_newline(text: str):
    """
    "This is a line."
    =>
    "This\nis\na\nline."
    """
    words = text.split()
    return "\n".join(words)
