import unittest

from task import open_and_print, open_and_double

file_content = """Roses are red.
Violets aren't blue.
It's literally in the name.
They're called violets.
"""


class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        with open("example.txt", "w") as f:
            f.write(file_content)

    def tearDown(self) -> None:
        with open("example.txt", "w") as f:
            f.write(file_content)

    def test_open_and_print(self):
        self.assertEqual(file_content, open_and_print(), msg="wrong answer")

    def test_open_and_double(self):
        open_and_double()
        with open("example.txt") as file:
            content = file.read()

        self.assertEqual(file_content+file_content, content, msg="wrong answer")
