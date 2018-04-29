"""
This module is used for the handling of opening, parsing, and closing the .bash_history text file.
"""
from os import path


def inspect_file_path(file_path):
    """
    This function performs inspections of a file path to validates that file path
    :param file_path: full path and filename to inspect
    :type file_path: str
    :return: 0 for valid file paths or a string for invalid file paths
    :rtype: int or str
    """

    if not path.exists(file_path):
        return f"File not found at {file_path}"

    # Make sure the file is not empty
    elif path.getsize(file_path) == 0:
        return f"{file_path} is empty"

    else:
        return 0
