# local library import
import descriptors as d
from logger_setup import ALogger

logger = ALogger().setup_logger()

def main():
    a = d.A()
    a.x = 6
    logger.debug("printing a: " + str(a.x))

    abc = d.B()
    abc.x = 7
    logger.debug("printing abc: " + str(abc.x))

    logger.debug("printing a again: " + str(a.x))

    class MyClass(object):
        x = d.RevealAccess()

    m = MyClass()
    m.x = 20
    logger.debug(m.x)


if __name__ == "__main__":
    main()
