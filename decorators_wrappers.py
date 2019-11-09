# standard library imports
from functools import wraps
from hashlib import sha256
from typing import AnyStr

# local imports
from util import logger

root = logger()


def log_me(func):
    root.info("The decorator is called during import. Not the wrapped function")

    @wraps(func)  # make sure the original function's name is retained
    def wrapped(
        *args, **kwargs
    ):  # wrap the original function; take all arguments, including func
        # this activity is executed when the function is called
        root.info("{} was called: {} {}".format(func.__name__, args, kwargs))
        # Encapsulate the original
        return func(*args, **kwargs)  # return the original function

    return wrapped  # Return the new wrapper


def override_me(func):
    root.info("The decorator is called during import. Not the wrapped function")

    @wraps(func)  # make sure the original function's name is retained
    def wrapped(
        *args, **kwargs
    ):  # wrap the original function; take all arguments, including func
        # this activity is executed when the function is called
        root.info("{} was called: {} {}".format(func.__name__, args, kwargs))
        # Encapsulate the original

        return lambda z: z + 1  # y no longer returns two. it returns a function

    return wrapped  # Return the new wrapper


@log_me  # notice that the decorator is not called with parentheses
def x(*args, **kwargs):
    root.info("Executing the body of function")
    return 1


@override_me  # notice that the decorator is not called with parentheses
def y(*args, **kwargs):
    root.info("Executing the body of function")
    return 1


def as_bytes(func):
    @wraps(func)
    def wrapped(*a):
        return func(*[q.encode() for q in a if isinstance(q, str)])

    return wrapped


@as_bytes
def hash_it(arg: AnyStr):
    return sha256(arg).hexdigest()


def decorator_factory(
    the_function_to_run_before_the_function_we_wrap,
):  # this returns a decorator, and thus is a decorator factory
    root.info("This runs upon import")

    def decorator(the_function_we_want_to_wrap):
        @wraps(the_function_we_want_to_wrap)
        def wrapped(*a):
            root.info(
                "Inside wrapped from hash_it_with_decorator_factory, before return"
            )
            # *** this is where you change the function you fed in
            return the_function_we_want_to_wrap(
                *[
                    the_function_to_run_before_the_function_we_wrap(t)
                    for t in a
                    if isinstance(t, str)
                ]
            )

        return wrapped  # we return a wrapped function

    return decorator  # return a decorator


@decorator_factory(lambda s: s.encode())
def hash_it_with_decorator_factory(arg: AnyStr):
    root.info("Inside hash_it_with_decorator_factory.")
    return sha256(arg).hexdigest()


class PreprocessArgumentWith:
    def __init__(self, the_function_to_run_before_the_function_we_wrap):
        root.info("Running the decorator factory class __init__")
        self.the_function_to_run_before_the_function_we_wrap = (
            the_function_to_run_before_the_function_we_wrap
        )

    def __call__(self, the_function_to_wrap):
        root.info("Running the decorator factory class __call__")

        @wraps(the_function_to_wrap)
        def wrapped(*a):
            root.info(
                "Inside wrapped from hash_it_with_decorator_class. This is called when the original function is called"
            )
            return the_function_to_wrap(
                # *** this is where you change the function you fed in
                *[
                    self.the_function_to_run_before_the_function_we_wrap(v)
                    for v in a
                    if isinstance(v, str)
                ]
            )

        return wrapped


@PreprocessArgumentWith(lambda s: s.encode())
def hash_it_with_decorator_class(arg: AnyStr):
    root.info("Inside hash_it_with_decorator_class")
    return sha256(arg).hexdigest()
