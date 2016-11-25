class LensError(ValueError):
    def __init__(self, name):
        self.name = name


class NotFound(LensError):
    def __str__(self):
        return "Did not find parser for {}".format(self.name)


class WrongFormat(LensError):
    def __str__(self):
        return "Parser {} does not have the correct format".format(self.name)


class LensNotConfigured(LensError):
    def __str__(self):
        return "Parser {} does not implement lens specifications".format(self.name)
