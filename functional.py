import functools
import os
from hashlib import sha256

# Functional programming
# Goal: using functions as arguments

# map is an operation on a sequence
sum(map(int, ["1", "2"]))

# this is the equivalent of
s = 0
for arg in ["1", "2"]:
    s += int(arg)

"""
functional: functions can be assigned to variables,
passed to other functions, or modified
- Declarative: express what we want; contrasts to 
imperative statements which express an action 
to carry out
- Stateless: output depends only on arguments;
and invokes no side effects; e.g. does not store date;
does not modify input; does not print anything
"""

# lambda can only include one line; one expression
# must calculate an single returnable expression
f = lambda x: x + 1
# roughly equivalent to

def f(x):
    return x + 1

# reduce accepts a function and a sequence
# reduce returns a single value
# Initially, the function is called with the first two items from the sequence and the result is returned.
# The function is then called again with the result obtained in step 1 and the next value in the sequence. This process keeps repeating until there are items in the sequence.
#
# functools.reduce(operator.add, vec)


def ensure_content(file, content):
    fp = sha256(content.encode()).hexdigest()
    if not os.path.isfile(fp):
        with open(fp, 'w') as fl:
            fl.write(content)
    os.link(fp, file)

