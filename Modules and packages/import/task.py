from greeting import Greeter, get_greeting, get_full_name


def task_get_full_name(first_name: str, last_name: str):
    # use the get_full_username() function from the greeting module
    # by importing it into this file, and return its result
    full_name = get_full_name(first_name, last_name)
    return full_name
