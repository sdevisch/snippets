# local library import
from logger_setup import ALogger

logger = ALogger().setup_logger()

"""
class A:
    @property
    def x(self):
        # access as a.x, not a.x()
        return self._x

is shorthand for the following
"""


class X(object):
    def __get__(self, obj, objtype):
        logger.debug("in __get__")
        if obj is None:
            logger.debug("obj is None. Returning instance")
            # Invoked via `A.x`
            # 'self' is the descriptor!
            return self  # return an instance of the class
        # Invoked via `A().x`
        logger.debug("Instance exists, returning property")
        return obj._x  # return the value of _x, an attribute of class X


class A(object):
    """
    Give the class an instance of our
    descriptor X.
    Instance x becomes a property
    """

    x = X()


class B(object):
    """
    Give the class an instance of our
    descriptor X.
    Instance x becomes a property
    """

    x = X()


class RevealAccess(object):
    """Logs during access"""

    def __init__(self):
        logger.debug("Initializing but not setting the property")
        # self.__set_name__(temperature)

    def __set_name__(self, owner, name):
        logger.debug("Setting the property")
        # Called when A.x = RevealAccess()
        # as self.__set_name__(A, 'x')
        self.name = name

    @property
    def attr(self):
        logger.debug("Returning the attribute")
        return f"_{self.name}"

    def __get__(self, obj, objtype):
        if obj is None:
            logger.info(f"Returning the instance {objtype}")
            return self
        logger.info(f"Retrieving {self.name}")
        return getattr(obj, self.attr)

    def __set__(self, obj, val):
        logger.info(f"Updating {self.name}")
        setattr(obj, self.attr, val)
