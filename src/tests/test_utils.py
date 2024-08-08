import unittest
import os
from utils import extract_properties, compare_and_write_differences
from config import extract_variables

class TestUtils(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Move up one directory to the project root
        cls.test_data_dir = os.path.join(cls.base_dir, 'test_data')
        cls.application_properties_file = os.path.join(cls.test_data_dir, 'application.properties')
        cls.environment_properties_file = os.path.join(cls.test_data_dir, 'environment.properties')
        cls.environment_op_properties_file = os.path.join(cls.base_dir, 'environment_op.properties')

    def test_extract_properties(self):
        properties = extract_properties(self.environment_properties_file)
        self.assertIn('env_variable', properties)
        self.assertEqual(properties['env_variable'], 'env_value')

    def test_compare_and_write_differences(self):
        compare_and_write_differences(self.application_properties_file, self.environment_properties_file, self.environment_op_properties_file)
        with open(self.environment_op_properties_file, 'r') as f:
            lines = f.readlines()
        self.assertGreater(len(lines), 0)

if __name__ == '__main__':
    unittest.main()
