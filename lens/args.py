import sys
import argparse

def parse_args():
    descr = "Extensible data structure traversal from the command line"

    parser = argparse.ArgumentParser(description=descr)
    parser.add_argument('--input', '-i', default=sys.stdin,
                        type=argparse.FileType('r'),
                        help='the input file (defaults to the standard input)')
    parser.add_argument('keys', metavar='key', nargs='*',
                        help='the keys to traverse')
    parser.add_argument('--format', '-f', default='json',
                        help='the data format to consume (defaults to json)')
    parser.add_argument('--no-highlight', '-n', type=bool,
                        help='prevent syntax highlighting')
    parser.add_argument('--formats', action='store_true',
                        help='print available formats')

    return parser.parse_args()
