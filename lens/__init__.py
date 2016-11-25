from lens.args       import parse_args
from lens.module     import find_module
from lens.runner     import run_module
from lens.exceptions import LensError
from lens.pp         import prettyprint
from lens.keys       import treat_keys

def run():
    args = parse_args()

    try:
        module = find_module(args.format)
    except LensError as e:
        print("lens encountered an error: {}".format(e))
        return

    keys = treat_keys(args.keys)

    treated = run_module(module, keys, args.input)

    if treated:
        prettyprint(module, treated)
