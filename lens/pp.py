import pygments
from pygments.formatters import TerminalFormatter

def prettyprint(module, output, no_highlight):
    if module.lexer and not no_highlight:
        output = pygments.highlight(output,
                                    module.lexer(),
                                    TerminalFormatter())

    if isinstance(output, bytes):
        print(output.decode("utf-8"))
    else:
        print(output)
