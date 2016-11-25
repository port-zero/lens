import sys

def run_module(module, keys, inpt):
    return module().treat(inpt.read(), keys)
