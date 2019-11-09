# import standard libraries
from contextlib import contextmanager
import logging
import os
import signal
import time


def logger(logpath="", filename=""):
    logpath = os.getcwd()
    filename = "log.txt"
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(funcName)20s() - %(message)s",
        level=logging.DEBUG,
        handlers=[
            logging.FileHandler("{0}/{1}.log".format(logpath, filename)),
            logging.StreamHandler(),
        ],
    )
    return logging

def log_to(logger_func):
    """A decorator to log every call to function (function name and arg values).
    logger_func should be a function that accepts a string and logs it
    somewhere. The default is logging.debug.
    If logger_func is None, then the resulting decorator does nothing.
    This is much more efficient than providing a no-op logger
    function: @log_to(lambda x: None).
    """
    if logger_func is not None:
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                for line in describe_call(func, *args, **kwargs):
                    logger_func(line)
                return func(*args, **kwargs)
            return wrapper
    else:
        decorator = lambda x: x
    return decorator

logdebug = log_to(logging.debug)

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


try:
    # Absent on Windows, trigger AttributeError
    signal.alarm
    print("in try")

    def _timeout(signum, frame):
        raise TimeoutError()

    signal.signal(signal.SIGALRM, _timeout)

    @contextmanager
    def timeout(seconds=1, message="Timeout!"):
        # NB: doesn't work on windows
        print("in timeout")
        signal.alarm(seconds)
        try:
            print("in yield")
            yield
        except TimeoutError:
            print("in timeouterror")
            raise TimeoutError(message)
            print("after raising error; this is never executed")
        finally:
            print("in finally; this is executed even if an error is raised")
            signal.alarm(0)


except AttributeError:

    @contextmanager
    def timeout(seconds=1, message="Timeout!"):
        t0 = time()
        yield
        if time() - t0 > seconds:
            raise TimeoutError(message)

