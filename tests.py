import unittest
import toml
from config3 import parse_toml, convert_to_ukya

class TestParseTOML(unittest.TestCase):

    def test_valid_toml(self):
        toml_input = '''
        [owner]
        name = "Tom"
        age = 35
        '''
        result = parse_toml(toml_input)
        expected = {'owner': {'name': 'Tom', 'age': 35}}
        self.assertEqual(result, expected)

class TestConvertToUkya(unittest.TestCase):

    def test_convert_list(self):
        value = [1, 2, 'three']
        result = convert_to_ukya(value)
        expected = '[ 1 2 "three" ]'
        self.assertEqual(result, expected)

    def test_convert_number(self):
        value = 3.14
        result = convert_to_ukya(value)
        expected = '3.14'
        self.assertEqual(result, expected)

    def test_convert_string(self):
        value = "Hello"
        result = convert_to_ukya(value)
        expected = '"Hello"'
        self.assertEqual(result, expected)

    def test_invalid_type(self):
        with self.assertRaises(ValueError):
            convert_to_ukya(None)
