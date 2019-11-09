# import standard packages
import time

# import local module
from contextmanager import write_signature, some_context, timeout

with write_signature('letter.txt', mode='w') as f:
    f.write("Hello!")

with some_context(1) as s:
    print("first in context manager " + str(s))
    print("second in context manager " + str(s))
print("third outside of context manager" + str(s))

with timeout() as t:
    print("We don't expect an error to be raised")
print("No error so far")

with timeout() as t:
    print("This is about to cause an error.")
    time.sleep(2)
    print("This will never run.")
print("This will never run either due to raised error")
