import xml.etree.ElementTree as ET

from  pygments.lexers.html import XmlLexer

from lens.parsers.base import LensParser

class Parser(LensParser):
    lexer = XmlLexer

    def treat(self, inpt, keys):
        loaded = ET.fromstring(inpt)

        for key in keys:
            if type(key) is int:
                loaded = loaded[key]
            else:
                loaded = loaded.find(key)

        return ET.tostring(loaded)
