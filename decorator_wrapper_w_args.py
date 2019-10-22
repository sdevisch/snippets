from functools import wraps
from logging import root


def logme(logger=root):
    def decorator(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            root.info(
                "{} was called: {} {}".format(
                    func.__name__, args, kwargs))
            # Encapsulate the original
            return func(*args, **kwargs)
        return wrapped  # Return the new wrapper
    return decorator


@logme
def x(*args, **kwargs):
    pass

# example from test exam
# takes any function and prints what it returns
def printme():
    def decorator(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            result = func(*args, **kwargs)
            print("The result was {}".format(result))
            return result
        return wrapped  # Return the new wrapper
    return decorator


@printme()
def my_fun(x):
    result = x + 1
    return result

@printme()
def squareme(x):
    result = x * x
    return result
