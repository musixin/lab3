import unittest
from lib import fib, bubble_sort, find_primes


class TestAlgorithms(unittest.TestCase):


    def test_fibonacci(self):
        self.assertEqual(fib(5), [0, 1, 1, 2, 3])
        self.assertEqual(fib(1), [0])
        self.assertEqual(fib(2), [0, 1])
        self.assertEqual(fib(0), [])
        self.assertEqual(fib(-3), [])
        with self.assertRaises(TypeError):
            fib("2")


    def test_bubble_sort(self):
        self.assertEqual(bubble_sort([3, 1, 2]), [1, 2, 3])
        self.assertEqual(bubble_sort([]), [])
        self.assertEqual(bubble_sort([5]), [5])
        self.assertEqual(bubble_sort([1, 2, 3]), [1, 2, 3])
        self.assertEqual(bubble_sort([3, 3, 1]), [1, 3, 3])
        with self.assertRaises(AttributeError):
            bubble_sort("2,3,4")
        with self.assertRaises(TypeError):
            bubble_sort([2.2, "string", 3.1, "", 5.0])


    def test_find_primes(self):
        self.assertEqual(find_primes(10), [2, 3, 5, 7])
        self.assertEqual(find_primes(3), [2])
        self.assertEqual(find_primes(2), [])
        self.assertEqual(find_primes(1), [])
        self.assertEqual(find_primes(0), [])
        self.assertEqual(find_primes(-10), [])
        with self.assertRaises(TypeError):
            find_primes(6.5)


if __name__ == '__main__':
    unittest.main()
