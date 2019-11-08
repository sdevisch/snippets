import util

log = util.logger()


def some_no_use_decorator(func):
    log.info("Some_no_use_decorator runs before some_func is defined")
    to_return = func
    log.info(
        "Some_func has been changed to potentially return something different. Some_func hasn't run yet"
    )
    return to_return


def some_func():
    log.info("The sum_func function doesn't get executed until after it's changed and called")
    return "Some_func now returns something"


# initialize dictionary
SUMMARIES = {}


def register(func, name=None):
    log.info("The decorator runs before anything else. Registering the function in a dictionary.")
    SUMMARIES[name or func.__name__] = func
    return func


@register                           # notice the syntax: no ()
def mean(x):
    log.info("In mean")
    numerator = sum(x)
    denominator = len(x)
    return numerator / denominator


def summarize(vec, stat="mean"):
    log.info("In summarize")
    return SUMMARIES[stat](vec)     # notice how we get the function from the dictionary and apply it to vec


log.info("After import, statements run before functions are defined")

# **** this is the start of the key step *** #
some_func = some_no_use_decorator(some_func)
# **** this is the start of the key step *** #

log.info("About to call some_func")
log.info(some_func())
