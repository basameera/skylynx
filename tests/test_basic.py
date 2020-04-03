import unittest
import os
import sys

sys.path.insert(0, os.getcwd())

import skylynx.text as txt

class TestCalc(unittest.TestCase):
    """ All functions should start with `test_` """

    def test_txt(self):
        self.assertEqual(txt.func(), 'hahahaha')


if __name__ == "__main__":
    unittest.main()
