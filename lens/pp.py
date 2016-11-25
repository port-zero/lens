import pygments
from pygments.formatters import TerminalFormatter

def prettyprint(module, output):
    if module.lexer:
        output = pygments.highlight(output,
                                    module.lexer(),
                                    TerminalFormatter())

    print(output)
