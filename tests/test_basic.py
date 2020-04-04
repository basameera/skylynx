import setup_path
import unittest

import skylynx.text as txt
import skylynx.utils as su


class TestCalc(unittest.TestCase):
    """ All functions should start with `test_` """

    def test_txt(self):
        self.assertEqual(txt.func(), 'hahahaha')

    def test_json(self):
        a = dict(
            a=123,
            b='skylynx'
        )
        su.json_write('example.json', a)
        b = su.json_read('example.json')
        self.assertEqual(a, b)

    def test_yaml(self):
        a = dict(
            a=123,
            b='skylynx'
        )
        su.yaml_write('example.yaml', a)
        b = su.yaml_read('example.yaml')
        self.assertEqual(a, b)


if __name__ == "__main__":
    unittest.main()
