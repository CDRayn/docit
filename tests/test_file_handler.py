"""
This module contains unit tests for validating the file_handlers.py module.
"""
import unittest
import os


from src.file_handler import inspect_file_path


class TestFilePathValidator(unittest.TestCase):
    """
    This class provides test cases against the logic used for validating a file path to a .bash_history file.
    """

    def test_file_exists(self):
        """
        This test case checks the logic used to determine if a file exists at a give file path.
        """
        empty_file = os.path.dirname(__file__) + '/test_files/empty_bash_history'
        valid_file_path = os.path.dirname(__file__) + '/test_files/valid_bash_history'
        invalid_file_path = '/this/path/does/not/exit'

        # Check that 0 is returned for a valid file
        self.assertEqual(
            inspect_file_path(valid_file_path),
            0
        )

        # Check that a message stating the file can not be found is returned for invalid file paths
        self.assertEqual(
            inspect_file_path(invalid_file_path),
            f"File not found at {invalid_file_path}"
        )

        # Check that a message stating the file is empty is returned for empty file paths
        self.assertEqual(
            inspect_file_path(empty_file),
            f"{empty_file} is empty"

        )


if __name__ == '__main__':
    unittest.main()
