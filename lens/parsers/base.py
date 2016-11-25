from lens.exceptions import LensNotConfigured

class LensParser():
    lexer = None

    def treat(self, inpt, keys):
        raise LensNotConfigured()
