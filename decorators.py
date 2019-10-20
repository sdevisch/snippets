from logging import root
import logging
import sys
from statistics import mean as arith_mean


SUMMARIES = {}


def register(func, name=None):
    # this never runs as the statements lowering the debug level to info have not run yet when this runs
    root.info("I'm logging in register and my name is: " + __name__)
    # the following does run
    print("I'm printing in register. This is run when the function mean is defined, not when it's called")
    print("This is run when the function mean is defined; not when it's called")
    print("As such, this is run when the module or the function is imported")

    # note that the function is registered under its name in the dictionary
    SUMMARIES[name or func.__name__] = func
    return func


@register
def mean(x):
    root.info("I'm in the logger for mean, and my name is: " + __name__)
    print("I'm printing in mean")
    return arith_mean(x)


def summarize(vec, stat='mean'):
    print(SUMMARIES[stat](vec))


def print_summaries():
    print(SUMMARIES)


# second example with data checks
import pandas as pd

DATA_CHECKS = {}


def register2(func, name=None):
    DATA_CHECKS[name or func.__name__] = func
    return func


@register2
def check_size():
    data = pd.DataFrame([0, 2, 3, 4])
    return data.shape[0] > 100


def list_checks():
    for name, check in DATA_CHECKS.items():
        print('{}: {}'.format(name, check()))


# prepare the logger to show INFO statements
log = logging.getLogger()
log.setLevel(logging.INFO)
stream = logging.StreamHandler(sys.stdout)
stream.setLevel(logging.INFO)
log.addHandler(stream)


