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

    def test_cli_args_dict_order(self):
        cli_params = dict(task=0, length=10)
        args = su.cli_args(cli_params)
        self.assertEqual(cli_params, args)

    def test_cli_args_number_of_args(self):
        with self.assertRaises(ValueError):
            import string
            alpha = list(string.ascii_lowercase)
            cli_params = dict(zip(alpha, alpha))
            su.cli_args(cli_params)

    def test_cli_args_input_type(self):
        with self.assertRaises(TypeError):
            cli_params = ['a', 'b']
            su.cli_args(cli_params)


if __name__ == "__main__":
    unittest.main()
