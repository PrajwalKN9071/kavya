import unittest
import os
from parser import main

class TestParser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Move up one directory to the project root
        cls.test_data_dir = os.path.join(cls.base_dir, 'src', 'test_data')
        cls.output_properties_file = os.path.join(cls.base_dir, 'src', 'output_properties.properties')
        cls.missing_properties_file = os.path.join(cls.base_dir, 'src', 'missing_properties.properties')
        cls.environment_op_properties_file = os.path.join(cls.base_dir, 'src', 'environment_op.properties')

    def test_main(self):
        main()
        self.assertTrue(os.path.isfile(self.output_properties_file))
        self.assertTrue(os.path.isfile(self.missing_properties_file))
        self.assertTrue(os.path.isfile(self.environment_op_properties_file))

        with open(self.output_properties_file, 'r') as f:
            lines = f.readlines()
        self.assertGreater(len(lines), 0)

        with open(self.missing_properties_file, 'r') as f:
            lines = f.readlines()
        self.assertGreater(len(lines), 0)

        with open(self.environment_op_properties_file, 'r') as f:
            lines = f.readlines()
        self.assertGreater(len(lines), 0)

if __name__ == '__main__':
    unittest.main()
