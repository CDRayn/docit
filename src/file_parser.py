"""
This module provides functionality for parsing an ASCII encoded .history_file and generating an in memory
object thatcan be searched and evaluated.
"""


class BashHistFile:
    """
    This class contains the methods and properties of an in memory object representing a .bash_history file
    """
    def __init__(self, file_path):
        """
        This is the constructor method of the class.
        :param file_path: fully qualified or relative file path to the .bash_history file
        :type file_path: str
        :returns: none
        """
        self.file_path = file_path
        self.lines = []

    def read_bash_hist_file(self):
        """
        This method reads a .bash_history_file and stores each line in a list
        """
        with open(self.file_path, mode='r') as file:
            data = file.read()

        for line_of_data in data:
            self.lines.append(line_of_data)
