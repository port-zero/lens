import pkg_resources

from lens.exceptions import NotFound, WrongFormat
from lens.parsers    import parsers

def get_and_print_formats():
    formats = list(parsers.keys())

    key = "lens-"
    keyl = len(key)
    for p in pkg_resources.working_set:
        if p.key.startswith(key) and p.key != 'lens-cli':
            formats.append(p.key[keyl:])

    print(", ".join(formats))


def find_module(name):
    if name in parsers:
        return parsers[name]

    return find_external(name)


def find_external(name):
    key = "lens-{}".format(name)
    modules = [p for p in pkg_resources.working_set
                 if p.key == key]

    if not modules:
        raise NotFound(name)

    module = __import__("lens_{}".format(name))

    if not hasattr(module, 'Parser'):
        raise WrongFormat(name)

    return getattr(module, 'Parser')
