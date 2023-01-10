import unittest

from task import task_get_full_name


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test_task_get_full_name(self):
        actual = task_get_full_name("John", "Doe")
        self.assertEqual("John Doe", actual, msg="names are not equal")
