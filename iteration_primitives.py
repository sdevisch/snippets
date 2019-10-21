# Comprehensions

a = [1, 1, 3]

b = [_ + 1 for _ in a]              # List

c = {str(_): _ for _ in a}          # Dict

uniques = {_ for _ in a}            # Set

# Careful... this is a generator!
d = (_ + 1 for _ in a)             # not a tuple!

# Functional
map(some_func, iterable)
filter(some_func, iterable)
functools.reduce(some_func, iterable)