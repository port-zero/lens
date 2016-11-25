import pip

from lens.exceptions import NotFound, WrongFormat
from lens.parsers    import parsers

def find_module(name):
    if name in parsers:
        return parsers[name]

    return find_by_pip(name)


def find_by_pip(name):
    key = "lens_{}".format(name)
    modules = [p for p in pip.get_installed_distributions()
                 if p.key == key]

    if not modules:
        raise NotFound(name)

    module = modules[0]

    if not hasattr(module, 'Parser'):
        raise WrongFormat(name)

    return getattr(module, 'Parser')
