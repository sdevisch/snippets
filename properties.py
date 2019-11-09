# standard library imports
from functools import wraps
import logging

# additional libraries
from scipy.sparse import csr_matrix

# local packages
from util import logger

logger = logger()


class SparseMatrix:
    @property
    def dense(self):
        # post process x
        return self._matrix.todense()

    # Use the new property object's decorators!
    @dense.setter
    def dense(self, val):
        # pre process x
        self._matrix = csr_matrix(val)


def logged_property(method):
    @property
    @wraps(method)
    def wrapped(self):
        logger.info("Accessing {}".format(method.__name__))
        return method(self)

    return wrapped


class A:
    @logged_property
    def x(self):
        return self._x

    @x.setter
    def x(self, val):
        # pre process x
        self._x = val

    @x.deleter
    def x(self):
        del self._x
