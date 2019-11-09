# import standard packages
import time
import util

log = util.logger()

# import local module
from context_w_log import write_signature, some_context, timeout

with write_signature('letter.txt', mode='w') as f:
    f.write("Hello!")

with some_context(1) as s:
    log.debug("first in context manager " + str(s))
    log.debug("second in context manager " + str(s))
log.debug("third outside of context manager" + str(s))

with timeout() as t:
    log.debug("We don't expect an error to be raised")
log.debug("No error so far")

with timeout() as t:
    try:
        log.debug("This is about to cause an error.")
        time.sleep(2)
    except TimeoutError:
        log.debug("A TimeoutError occured.")
log.debug("after testing timeout")
