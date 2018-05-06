"""
This module contains unit tests for validating the file_parser.py module
"""
import os
import unittest


from src.file_parser import BashHistFile


class TestBashHistFile(unittest.TestCase):
    """
    This class is used to validate the methods of the BashHistFile class.
    """
    bash_hist_fixture = os.path.dirname(__file__) + '/test_files/valid_bash_history'
    test_lines = [
        'docker image ls',
        'docker pull redis',
        'docker image ls',
        'docker run -it --name redis redis:latest',
        'docker container ls -a',
        'docker container rm redis',
        'ls',
        'cd ~',
        'ls',
    ]

    def test_read_bash_hist_file(self):
        """
        This method is used to validate the BashHistFile.read_bash_hist_file() method
        """
        bash_hist_file = BashHistFile(self.bash_hist_fixture)

        # Ensure bash_hist_file.lines is empty
        self.assertFalse(bash_hist_file.lines)

        bash_hist_file.read_bash_hist_file()
        self.assertEqual(bash_hist_file.lines, self.test_lines, msg=bash_hist_file.lines)


# If this module is directly executed, run all its unit tests
if __name__ == '__main__':
    unittest.main()
