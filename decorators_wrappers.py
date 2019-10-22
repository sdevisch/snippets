from functools import wraps
from logging import root
def logme(func):
    # Create a new function
    @wraps(func)
    def wrapped(*args, **kwargs):
        root.info(
            "{} was called: {} {}".format(
                func.__name__, args, kwargs))
        # Encapsulate the original
        return func(*args, **kwargs)
    return wrapped  # Return the new wrapper


@logme                                          # notice that this decorator is not called with parentheses
def x(*args, **kwargs):
pass
x(1, a=24)
# x was called: (1,) {'a': 24}

