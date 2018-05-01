"""
This is the main executable for DocIt.
"""
import argparse


# Setup command line argument parsing
parser = argparse.ArgumentParser()
parser.add_argument("path", help="file path to .bash_history file to parse")
parser.add_argument(
    "-f",
    "--format",
    choices=["md", "rst"],
    help="format of output, options are md for Markdown and rst for reStructuredText",
)

args = parser.parse_args()
