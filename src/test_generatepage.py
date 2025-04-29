import unittest
from generatepage import extract_title

class TestGeneratePage(unittest.TestCase):

    def test_extract_title(self):
        md = """
This text shouldn't be chosen

# This text header should be chosen
## This one should not

This should not be chosen either
"""

        title = extract_title(md)
        self.assertEqual(
            title, "This text header should be chosen",
        )

    def test_extract_title2(self):
        md = """
# This text header should be chosen
## This one should not
### This should not be chosen as well

This should not be chosen either
"""

        title = extract_title(md)
        self.assertEqual(
            title, "This text header should be chosen",
        )

    def test_extract_titleE(self):
        md = """
This text header should be chosen
## This one should not
### This should not be chosen as well

This should not be chosen either
"""

        with self.assertRaises(Exception): extract_title(md)