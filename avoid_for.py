import util

from util import logger
log = logger()


def add_x_to_list(adder=1, add_to=(0, 1, 2, 3)):
    return [_ + adder for _ in add_to]  # list comprehension

