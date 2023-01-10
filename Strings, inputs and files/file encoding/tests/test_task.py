import unittest

from task import fix_encoding


expected_content = """Roses are räd.
Violets aren't blüe.
It's literally in the name.
They're called violets.
"""

filename = "example.txt"

class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        with open(filename, "w") as f:
            f.write(expected_content)

    def test_fix_encoding(self):
        fix_encoding(filename)
        with open(filename, "r", encoding="utf-8") as file:
            actual_content = file.read()

        self.assertEqual(actual_content, expected_content, "wrong answer")