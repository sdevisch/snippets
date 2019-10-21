
# Modules vs. packages
# from https://docs.python.org/3/tutorial/modules.html

# A module is a file containing Python definitions and statements.
# The file name is the module name with the suffix .py appended.
# Within a module, the module’s name (as a string) is available as the value of the global variable __name__.

# Fibonacci numbers module
# this is a python definition; a definition of a function
def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result


# these are statements, not python definitions. They get executed when the modules is run or imported
if __name__ == "__main__":
    print("I execute when run from the command line. My __name__ is not set to the name of the .py file: " + __name__)
    import sys
    fib(int(sys.argv[1]))
else:
    print("I execute when my module is imported in the interpreter. My __name__ is set to the name of the .py file: " + __name__)

# you can use this module from the python interpreter
# >>> import modules
# This does not enter the names of the functions defined in modules directly in the current symbol table;
# it only enters the module name modules there.
# Using the module name you can access the functions fib() and fib2()

# you can also use this module from the command line
# $ python modules.py 50

# The built-in function dir() is used to find out which names a module defines.
# It returns a sorted list of strings
# >>> dir(modules)

# dir() does not list the names of built-in functions and variables.
# If you want a list of those, they are defined in the standard module builtins:
# >>> import builtins
# >>> dir(builtins)


# a package is a collection of modulesPackages
# they are a way of structuring Python’s module namespace by using “dotted module names”.
# For example, the module name A.B designates a submodule named B in a package named A.
# Modules save authors of different modules from having to worry about each other’s global variable names,
# Similarly dotted module names saves authors from having to worry about each other’s module names.

# !!!!!!
# The __init__.py file is required for Python to treat dirs as packages.

