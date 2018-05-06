"""
This module contains unit tests for validating the file_handlers.py module.
"""
import os
import unittest

from unittest.mock import patch

from src.file_handler import inspect_file_path


class TestFilePathValidator(unittest.TestCase):
    """
    This class provides test cases against the logic used for validating a file path to a .bash_history file.
    """
    empty_file = os.path.dirname(__file__) + '/test_files/empty_bash_history'
    jpeg_file = '/home/john_doe/Pictures/dog.jpg'
    valid_file_path = os.path.dirname(__file__) + '/test_files/valid_bash_history'
    invalid_file_path = '/this/path/does/not/exist'

    def test_file_exists(self):
        """
        This test case checks the logic used to determine if a file exists at a give file path.
        """

        # Check that 0 is returned for a valid file
        self.assertEqual(
            inspect_file_path(file_path=self.valid_file_path),
            0
        )

        # Check that a message stating the file can not be found is returned for invalid file paths
        self.assertEqual(
            inspect_file_path(file_path=self.invalid_file_path),
            f"File not found at {self.invalid_file_path}."
        )

        # Check that a message stating the file is empty is returned for empty file paths
        self.assertEqual(
            inspect_file_path(file_path=self.empty_file),
            f"{self.empty_file} is empty."

        )

    @patch('magic.from_file')
    def test_valid_file_type(self, mock_magic_from_file):
        """
        This test case checks the logic used to determine if the file is a valid ASCII text encoded file
        """
        mock_magic_from_file.return_value = 'ASCII text'

        self.assertEqual(
            inspect_file_path(file_path=self.valid_file_path),
            0
        )

    @patch('magic.from_file')
    @patch('os.path.exists')
    @patch('os.path.getsize')
    def test_invalid_file_type(self, mock_magic_from_file, mock_path_exists, mock_path_getsize):
        """
        This test case checks the logic used to determine if the file is not a valid ASCII text encode files
        """
        mock_magic_from_file.return_value = 'JPEG image data, JFIF standard 1.01'
        mock_path_exists.return_value = True
        mock_path_getsize.return_value = 100000

        self.assertEqual(
            inspect_file_path(file_path=self.jpeg_file),
            f"{self.jpeg_file} is not a valid .bash_history file."
        )


# If this module is directly executed, run all its unit tests
if __name__ == '__main__':
    unittest.main()
