

from contextlib import contextmanager

import util

log = util.logger()


@contextmanager
def write_signature(*args, **kwargs):
    with open(*args, **kwargs) as f:
        yield f
        f.write('\n\nSincerely,\n\n-Steven')


@contextmanager
def some_context(provided_number):
    print("in the context")
    try:
        print("in try")
        yield provided_number + 1    # must be a yield statement
    except KeyboardInterrupt:
        print("in except")
        raise
    finally:
        print("in finally")



