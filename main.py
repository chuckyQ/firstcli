"""
Usage:
  main.py [options] <program>
  main.py (-h | --help | --version)

Options:
  -c, --compiled  Compile source to machine code
  -h, --help      Show this help screen and exit
  --version       Give version of tool
"""

__version__ = '0.0.1'

from docopt import docopt

opts = options = docopt(__doc__, version=__version__)

if opts['--compiled']:

	print('Compiling to machine code')
