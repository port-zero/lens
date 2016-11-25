import pygments
from pygments.formatters import TerminalFormatter

def prettyprint(module, output):
    print(pygments.highlight(output, module.lexer(), TerminalFormatter()))
