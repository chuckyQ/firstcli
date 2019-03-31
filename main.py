"""
Usage:
  main.py (-h | --help | --version)

Options:
  -h, --help    Show this help screen and exit
  --version     Give version of tool
"""


from docopt import docopt

doc = docopt(__doc__)
print(doc)