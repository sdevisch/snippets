

from contextlib import contextmanager
import signal
import time


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

