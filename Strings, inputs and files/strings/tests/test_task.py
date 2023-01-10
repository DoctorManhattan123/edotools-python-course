import unittest

from task import list_all_chars
from task import print_every_word_in_newline


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test_list_all_chars(self):
        self.assertEqual(['t', 'e', 'x', 't'], list_all_chars("text"), msg="wrong answer")
        self.assertEqual(['o', 't', 'h', 'e', 'r', ' ', 't', 'e', 'x', 't'], list_all_chars("other text"), msg="wrong answer")

def test_print_every_word_in_newline(self):
        self.assertEqual("all\n3\nwords", print_every_word_in_newline("all 3 words"), msg="wrong answer")
