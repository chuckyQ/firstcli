"""
Usage:
  main.py (-h | --help | --version)

Options:
  -h, --help    Show this help screen and exit
  --version     Give version of tool
"""

__version__ = '0.0.1'

from docopt import docopt

doc = docopt(__doc__, version=__version__)
