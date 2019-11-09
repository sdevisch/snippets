from contextmanager import write_signature, some_context

with write_signature('letter.txt', mode='w') as f:
    f.write("Hello!")

with some_context(1) as s:
    print("first in context manager " + str(s))
    print("second in context manager " + str(s))
print("third outside of context manager" + str(s))
