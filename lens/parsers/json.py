import json

from  pygments.lexers.data import JsonLexer

from lens.parsers.base import LensParser

class Parser(LensParser):
    lexer = JsonLexer

    def treat(self, inpt, keys):
        loaded = json.loads(inpt)

        for key in keys:
            loaded = loaded[key]

        return json.dumps(loaded, indent=2)
