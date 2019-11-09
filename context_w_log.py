

from contextlib import contextmanager
import signal
import time
import util

log = util.logger()

@contextmanager
def write_signature(*args, **kwargs):
    with open(*args, **kwargs) as f:
        yield f
        f.write('\n\nSincerely,\n\n-Steven')


@contextmanager
def some_context(provided_number):
    log.debug("in the context")
    try:
        log.debug("in try")
        yield provided_number + 1    # must be a yield statement
    except KeyboardInterrupt:
        log.debug("in except")
        raise
    finally:
        log.debug("in finally")


try:
    # Absent on Windows, trigger AttributeError
    signal.alarm
    log.debug("in try")

    def _timeout(signum, frame):
        raise TimeoutError()

    signal.signal(signal.SIGALRM, _timeout)

    @contextmanager
    def timeout(seconds=1, message="Timeout!"):
        # NB: doesn't work on windows
        log.debug("in timeout")
        signal.alarm(seconds)
        try:
            log.debug("in yield")
            yield
        except TimeoutError:
            log.debug("in timeouterror")
            raise TimeoutError(message)
            log.debug("after raising error; this is never executed")
        finally:
            log.debug("in finally; this is executed even if an error is raised")
            signal.alarm(0)


except AttributeError:

    @contextmanager
    def timeout(seconds=1, message="Timeout!"):
        t0 = time()
        yield
        if time() - t0 > seconds:
            raise TimeoutError(message)

