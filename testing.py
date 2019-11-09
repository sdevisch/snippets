
from unittest import TestCase
from util import timeout

def optimized_fibonacci(max_fib):
    # initialize with first two numbers
    fib_result, fib_next = 0, 1

    # produce the fibonacci sequence in a non-recursive way
    for _ in range(max_fib):
        fib_result, fib_next = fib_next, fib_result + fib_next
    return fib_result


class FibTests(TestCase):
    def test_fibonnacci(self):
        for n, expected in [
            (0, 0),
            (1, 1),
            (100, 354224848179261915075),
        ]:
            with timeout():
                self.assertEqual(expected, optimized_fibonacci(n))