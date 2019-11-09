# local package
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

class X:
    def __get__(self, obj, objtype):
        print("in __get__")
        if obj is None:
            logger.debug("obj is None. Returning instance")
            # Invoked via `A.x`
            # 'self' is the descriptor!
            return self  # return an instance of the class
        # Invoked via `A().x`
        logger.debug("Instance exists, returning property")
        return obj._x  # return the value of _x, an attribute of class X


class A:
    x = X()


