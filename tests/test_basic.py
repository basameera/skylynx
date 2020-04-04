import setup_path
import unittest

import skylynx.utils as su
import os
import shutil


class TestCalc(unittest.TestCase):
    """ All functions should start with `test_` """

    def test_json(self):
        a = dict(
            a=123,
            b='skylynx'
        )
        su.json_write('example.json', a)
        b = su.json_read('example.json')
        self.assertEqual(a, b)
        os.remove('example.json')

    def test_yaml(self):
        a = dict(
            a=123,
            b='skylynx'
        )
        su.yaml_write('example.yaml', a)
        b = su.yaml_read('example.yaml')
        self.assertEqual(a, b)
        os.remove('example.yaml')

    def test_makedirs(self):
        path = 'path/to/the/folder/'
        su.makedirs(path)
        self.assertTrue(os.path.exists(path))
        os.removedirs(path)


if __name__ == "__main__":
    unittest.main()
