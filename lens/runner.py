import sys

def run_module(module, keys, inpt):
    try:
        return module().treat(inpt.read(), keys)
    except KeyError as e:
        print("Key {} not found".format(e))
    except Exception as e:
        print("The traversal failed with the exception: {}".format(e))
